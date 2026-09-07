#!/usr/bin/env python3
"""Offline local-link, heading-anchor, fence, and portable skill metadata checks.

Uses a CommonMark parser (with tables) and PyYAML, not regular expressions to
parse Markdown or YAML. This is a repository check, not a harness certification.
"""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

try:
    from markdown_it import MarkdownIt
    import yaml
except ImportError:
    raise SystemExit("Missing check dependencies. Use Python 3.10+ and run: "
                     "python -m pip install -r scripts/requirements-checks.txt")


EXCLUDED = {".git", "work", ".venv", "node_modules", "__pycache__"}
SKILL_PATH = Path("skills/vibe-code-docs-stack")
MARKDOWN = MarkdownIt("commonmark").enable("table")


class UniqueSafeLoader(yaml.SafeLoader):
    """Safe YAML parsing that also rejects silently overwritten duplicate keys."""


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str):
            raise yaml.constructor.ConstructorError(None, None, "mapping keys must be strings", key_node.start_mark)
        if key in result:
            raise yaml.constructor.ConstructorError(None, None, f"duplicate key: {key}", key_node.start_mark)
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


class HTMLReferences(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.anchors = set()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in (("id", "name") if tag == "a" else ("id",)):
            if attrs.get(key):
                self.anchors.add(attrs[key])
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append((attrs[key], self.getpos()[0]))

    handle_startendtag = handle_starttag


def frontmatter(text):
    """Return YAML and body, retaining original line numbers in the body."""
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None, text
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return "".join(lines[1:index]), "\n" * (index + 1) + "".join(lines[index + 1:])
    return None, text


def visible_text(tokens):
    text = []
    for token in tokens:
        if token.children:
            text.append(visible_text(token.children))
        elif token.type in ("text", "code_inline"):
            text.append(token.content)
        elif token.type in ("softbreak", "hardbreak"):
            text.append(" ")
    return "".join(text)


def heading_slug(text):
    # GitHub-style headings used in this repository: lowercase; remove markup
    # punctuation; preserve letters, numbers, underscores and hyphens.
    return re.sub(r"[^\w\- ]", "", text.lower()).replace(" ", "-")


def parse_markdown(text):
    _, body = frontmatter(text)
    tokens = MARKDOWN.parse(body)
    anchors, used, links, problems = set(), set(), [], []
    lines = body.splitlines()
    for index, token in enumerate(tokens):
        line = token.map[0] + 1 if token.map else 1
        if token.type == "heading_open":
            slug = heading_slug(visible_text(tokens[index + 1].children or []))
            base, suffix = slug, 0
            while slug in used:
                suffix += 1
                slug = f"{base}-{suffix}"
            used.add(slug)
            anchors.add(slug)
        if token.type == "fence":
            # CommonMark permits an unclosed fence through EOF; this repository
            # requires a closing fence so a later edit cannot disappear into it.
            closing = lines[token.map[1] - 1] if token.map else ""
            closing = re.sub(r"^\s*(?:>\s*)*", "", closing)
            closing_pattern = re.escape(token.markup[0]) + "{" + str(len(token.markup)) + r",}\s*"
            if not re.fullmatch(closing_pattern, closing) or token.map[1] == token.map[0] + 1:
                problems.append((line, "unclosed fenced code block"))
        children = token.children or [token]
        for child in children:
            if child.type == "link_open":
                links.append((child.attrGet("href"), line))
            elif child.type == "image":
                links.append((child.attrGet("src"), line))
            elif child.type in ("html_inline", "html_block"):
                html = HTMLReferences()
                html.feed(child.content)
                anchors.update(html.anchors)
                links.extend((url, line + offset - 1) for url, offset in html.links)
    return anchors, links, problems


def markdown_files(root):
    """Visit dot-directories such as .github, skipping only local scratch/tooling."""
    for path in sorted(root.rglob("*.md")):
        if not any(part in EXCLUDED for part in path.relative_to(root).parts) and path.is_file():
            yield path


def check_markdown(root, package=None):
    root = Path(root).resolve()
    package = Path(package).resolve() if package else None
    errors, documents = [], {}
    for path in markdown_files(root):
        label = path.relative_to(root)
        if path.is_symlink():
            errors.append(f"{label}: Markdown symlink is not portable")
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            errors.append(f"{label}: cannot read UTF-8 Markdown ({error})")
            continue
        anchors, links, problems = parse_markdown(content)
        if path.name == "CLAUDE.md":
            links.extend((match.group(1), line) for line, text in enumerate(content.splitlines(), 1)
                         if (match := re.fullmatch(r"\s*@([^\s]+)\s*", text)))
        documents[path] = (anchors, links)
        errors.extend(f"{label}:{line}: {message}" for line, message in problems)

    checked = 0
    for source, (_, links) in documents.items():
        boundary = package if package and source.is_relative_to(package) else root
        for url, line in links:
            label = f"{source.relative_to(root)}:{line}"
            try:
                parsed = urlsplit(url)
            except ValueError:
                errors.append(f"{label}: malformed link: {url}")
                continue
            if parsed.scheme or parsed.netloc:
                if parsed.scheme == "file" or (len(parsed.scheme) == 1 and parsed.path.startswith(("/", "\\"))):
                    errors.append(f"{label}: nonportable filesystem link: {url}")
                continue  # No network access, including HTTP, mailto and data URLs.
            checked += 1
            local = unquote(parsed.path)
            if local.startswith(("/", "\\")) or "\\" in local:
                errors.append(f"{label}: use a portable relative path: {url}")
                continue
            target = (source.parent / local).resolve() if local else source
            if not target.is_relative_to(boundary):
                errors.append(f"{label}: link escapes {'skill package' if boundary == package else 'repository'}: {url}")
                continue
            if not target.exists():
                errors.append(f"{label}: missing local target: {url}")
                continue
            fragment = unquote(parsed.fragment)
            if not fragment:
                continue
            if target.is_dir():
                target = target / "README.md"
            if target in documents:
                if fragment not in documents[target][0]:
                    errors.append(f"{label}: missing heading or HTML anchor: {url}")
            elif (match := re.fullmatch(r"L([1-9]\d*)(?:-L([1-9]\d*))?", fragment)) and target.is_file():
                start, end = int(match.group(1)), int(match.group(2) or match.group(1))
                try:
                    count = len(target.read_text(encoding="utf-8").splitlines())
                    if not 1 <= start <= end <= count:
                        errors.append(f"{label}: line anchor outside target: {url}")
                except (OSError, UnicodeError):
                    errors.append(f"{label}: cannot check line anchor: {url}")
            else:
                errors.append(f"{label}: cannot resolve fragment on this target: {url}")
    return errors, len(documents), checked


def load_yaml(text, label, errors):
    try:
        value = yaml.load(text, Loader=UniqueSafeLoader)
        if not isinstance(value, dict):
            errors.append(f"{label}: expected a YAML mapping")
            return {}
        return value
    except yaml.YAMLError as error:
        mark = getattr(error, "problem_mark", None)
        detail = getattr(error, "problem", None) or "invalid YAML"
        errors.append(f"{label}:{mark.line + 1 if mark else 1}: {detail}")
        return {}


def check_skill(skill):
    """Check portable frontmatter plus this package's version/license/UI contract."""
    skill = Path(skill)
    errors = []
    if not skill.is_dir() or skill.is_symlink():
        return ["Skill directory is missing or is a symlink"], None
    for path in skill.rglob("*"):
        if path.is_symlink():
            errors.append(f"{path.relative_to(skill)}: symlinks are not supported in the standalone package")
    for required in ("SKILL.md", "LICENSE"):
        if not (skill / required).is_file() or (skill / required).is_symlink():
            errors.append(f"{required}: required regular file is missing")
    if errors:
        return errors, None
    try:
        header, body = frontmatter((skill / "SKILL.md").read_text(encoding="utf-8"))
        if header is None:
            return ["SKILL.md: expected opening and closing YAML frontmatter delimiters"], None
        if not body.strip():
            errors.append("SKILL.md: Markdown instructions are missing after the frontmatter")
        data = load_yaml(header, "SKILL.md", errors)
        allowed = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
        for key in sorted(data.keys() - allowed):
            errors.append(f"SKILL.md: unsupported portable frontmatter field: {key}")
        name = data.get("name")
        if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
            errors.append("SKILL.md: name must be 1–64 lowercase letters/digits with single interior hyphens")
        elif name != skill.name:
            errors.append("SKILL.md: name must match the containing skill directory")
        for key, limit in (("description", 1024), ("compatibility", 500), ("license", None), ("allowed-tools", None)):
            if key not in data and key != "description":
                continue
            value = data.get(key)
            if not isinstance(value, str) or not value.strip() or (limit and len(value) > limit):
                errors.append(f"SKILL.md: {key} must be a nonempty string" + (f" of at most {limit} characters" if limit else ""))
        metadata = data.get("metadata", {})
        if not isinstance(metadata, dict) or any(not isinstance(v, str) for v in metadata.values()):
            errors.append("SKILL.md: metadata must map string keys to string values")
            metadata = {}
        version = metadata.get("version")
        if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", version):
            errors.append("SKILL.md: this package requires metadata.version as a quoted release version, e.g. 0.2.0")
        if data.get("license") != "MIT":
            errors.append("SKILL.md: this package's license must be MIT")
        ui = skill / "agents/openai.yaml"
        if ui.exists():
            if not ui.is_file():
                errors.append("agents/openai.yaml: expected a regular file")
            else:
                value = load_yaml(ui.read_text(encoding="utf-8"), "agents/openai.yaml", errors)
                interface = value.get("interface", {})
                if not isinstance(interface, dict):
                    errors.append("agents/openai.yaml: interface must be a mapping")
                else:
                    for key in ("display_name", "short_description", "default_prompt"):
                        if not isinstance(interface.get(key), str) or not interface[key].strip():
                            errors.append(f"agents/openai.yaml: interface.{key} must be a nonempty string")
                    prompt = interface.get("default_prompt", "")
                    if isinstance(prompt, str) and isinstance(name, str) and not re.search(r"\$" + re.escape(name) + r"(?![\w-])", prompt):
                        errors.append("agents/openai.yaml: default_prompt must mention this skill's $name")
        return errors, version
    except (OSError, UnicodeError) as error:
        return errors + [f"Cannot read skill metadata: {error}"], None


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="Toolkit repository root")
    parser.add_argument("--skill", type=Path, help="Check only a standalone skill directory, including its internal links")
    args = parser.parse_args(argv)
    root = (args.skill or args.root).resolve()
    skill = args.skill.resolve() if args.skill else root / SKILL_PATH
    errors, version = check_skill(skill)
    link_errors, count, links = check_markdown(root, skill)
    errors.extend(link_errors)
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Checked {count} Markdown files and {links} local links; skill version {version or 'unknown'}; {len(errors)} problems. "
          "External URLs and live harness behavior were not checked.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
