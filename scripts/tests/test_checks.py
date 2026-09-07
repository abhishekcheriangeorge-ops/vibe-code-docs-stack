"""Isolated positive/negative fixtures for maintainer checks; no network or app data."""

from contextlib import redirect_stderr, redirect_stdout
import io
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from build_skill_assets import bundle
from check_docs import check_markdown, check_skill, main, parse_markdown


HEADER = """---
name: vibe-code-docs-stack
description: Create and maintain project documentation.
license: MIT
metadata:
  version: "0.2.0"
---

# Skill

[Guide](references/guide.md#first-task)
"""


class Fixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.skill = self.root / "skills/vibe-code-docs-stack"

    def write(self, path, text):
        out = self.root / path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
        return out

    def seed_skill(self):
        self.write("skills/vibe-code-docs-stack/SKILL.md", HEADER)
        self.write("skills/vibe-code-docs-stack/LICENSE", "MIT License\n")
        self.write("skills/vibe-code-docs-stack/references/guide.md", "# First task\n")

    def seed_assets(self):
        self.write("LICENSE", "MIT License\nCopyright fixture\n")
        self.write("starter-kit/NOW.md", "# Current state\n")
        self.write("starter-kit/templates/RUNBOOK.md", "# Runbook\n")
        self.write("starter-kit/.github/pull_request_template.md", "# Review\n")
        self.write("starter-kit/ADOPTING-THIS-KIT.md", "Not bundled.\n")
        with redirect_stdout(io.StringIO()):
            errors, _, _ = bundle(self.root)
        self.assertEqual(errors, [])


class MarkdownTests(Fixture):
    def test_links_references_images_html_and_duplicate_unicode_headings(self):
        self.write("guide (copy).md", "# Café & `setup`\n\n# Repeat\n\n# Repeat\n\n<a id='manual'></a>\n")
        self.write("image.png", "fixture")
        self.write("README.md", """# Readme
[inline](<guide (copy).md#café--setup>)
[reference][guide]
![image](image.png)
<a href="guide%20(copy).md#manual">HTML</a>

[guide]: guide%20(copy).md#repeat-1

`[code](missing.md)`

```md
[example](also-missing.md)
```
""")
        errors, count, links = check_markdown(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(count, 2)
        self.assertEqual(links, 4)

    def test_missing_target_anchor_and_unclosed_fence_are_all_reported(self):
        self.write("README.md", "# Readme\n[missing](missing.md)\n[anchor](#absent)\n\n```sh\necho sample\n")
        errors, _, _ = check_markdown(self.root)
        self.assertTrue(any("missing local target" in e for e in errors), errors)
        self.assertTrue(any("missing heading" in e for e in errors), errors)
        self.assertTrue(any("unclosed fenced" in e for e in errors), errors)

    def test_longer_closing_fence_and_setext_headings(self):
        anchors, _, errors = parse_markdown("Setext title\n============\n\n~~~text\ncontent\n~~~~\n")
        self.assertEqual(errors, [])
        self.assertIn("setext-title", anchors)

    def test_package_escape_fails_even_when_repository_target_exists(self):
        self.seed_skill()
        self.write("README.md", "# Root\n")
        guide = self.skill / "references/guide.md"
        guide.write_text("# First task\n[escape](../../../README.md)\n", encoding="utf-8")
        errors, _, _ = check_markdown(self.root, self.skill)
        self.assertTrue(any("link escapes skill package" in e for e in errors), errors)

    def test_detached_skill_checks_without_parent_repo(self):
        self.seed_skill()
        detached = self.root / "detached/vibe-code-docs-stack"
        shutil.copytree(self.skill, detached)
        shutil.rmtree(self.root / "skills")
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            self.assertEqual(main(["--skill", str(detached)]), 0)

    def test_claude_import_and_nonportable_local_links(self):
        self.write("CLAUDE.md", "@missing.md\n")
        self.write("README.md", '<a href="file:///tmp/private.md">local</a>\n[absolute](/tmp/file.md)\n')
        errors, _, _ = check_markdown(self.root)
        self.assertEqual(len(errors), 3, errors)

    def test_network_urls_are_skipped_and_code_line_anchors_checked(self):
        self.write("sample.py", "one\ntwo\n")
        self.write("README.md", "[web](https://invalid.invalid/no-network)\n[line](sample.py#L2)\n[bad](sample.py#L3)\n")
        errors, _, links = check_markdown(self.root)
        self.assertEqual(links, 2)
        self.assertEqual(len(errors), 1, errors)
        self.assertIn("line anchor outside target", errors[0])


class MetadataTests(Fixture):
    def test_valid_metadata(self):
        self.seed_skill()
        self.assertEqual(check_skill(self.skill), ([], "0.2.0"))

    def test_yaml_invalid_duplicate_and_unsafe_tag_rejected(self):
        self.seed_skill()
        for payload in ("name: [broken", "name: one\nname: two", "name: !!python/object/apply:os.system ['do-not-run']"):
            with self.subTest(payload=payload):
                (self.skill / "SKILL.md").write_text(f"---\n{payload}\n---\n# Body\n", encoding="utf-8")
                errors, _ = check_skill(self.skill)
                self.assertTrue(errors)
                self.assertTrue(any("duplicate key" in e or "expected" in e or "constructor" in e for e in errors), errors)

    def test_wrong_name_nonstring_metadata_and_unknown_field_rejected(self):
        self.seed_skill()
        text = HEADER.replace("name: vibe-code-docs-stack", "name: other-skill\nunportable: true").replace('version: "0.2.0"', "version: 2")
        (self.skill / "SKILL.md").write_text(text, encoding="utf-8")
        errors, _ = check_skill(self.skill)
        self.assertTrue(any("directory" in e for e in errors), errors)
        self.assertTrue(any("string values" in e for e in errors), errors)
        self.assertTrue(any("unsupported portable" in e for e in errors), errors)

    def test_optional_ui_mapping_and_prompt_name(self):
        self.seed_skill()
        self.write("skills/vibe-code-docs-stack/agents/openai.yaml", """interface:
  display_name: Example
  short_description: Example skill
  default_prompt: Use $vibe-code-docs-stack-wrong
""")
        errors, _ = check_skill(self.skill)
        self.assertTrue(any("$name" in e for e in errors), errors)

    def test_empty_instruction_body_is_rejected(self):
        self.seed_skill()
        (self.skill / "SKILL.md").write_text(HEADER.split("# Skill")[0], encoding="utf-8")
        errors, _ = check_skill(self.skill)
        self.assertTrue(any("instructions are missing" in e for e in errors), errors)

    def test_missing_license_and_symlink_are_rejected(self):
        self.seed_skill()
        (self.skill / "LICENSE").unlink()
        (self.skill / "outside.md").symlink_to(self.root / "private.md")
        errors, _ = check_skill(self.skill)
        self.assertTrue(any("LICENSE" in e for e in errors), errors)
        self.assertTrue(any("symlink" in e for e in errors), errors)


class AssetTests(Fixture):
    def test_generation_includes_hidden_template_and_mit_notice(self):
        self.seed_assets()
        target = self.skill / "assets/templates"
        self.assertTrue((target / ".github/pull_request_template.md").is_file())
        self.assertFalse((target / "ADOPTING-THIS-KIT.md").exists())
        self.assertEqual((self.skill / "LICENSE").read_bytes(), (self.root / "LICENSE").read_bytes())
        self.assertEqual(bundle(self.root, check=True), ([], 3, 0))

    def test_check_reports_extra_stale_and_missing_without_writing(self):
        self.seed_assets()
        self.write("starter-kit/NOW.md", "# Changed\n")
        self.write("starter-kit/NEW.md", "# New\n")
        extra = self.write("skills/vibe-code-docs-stack/assets/templates/stray.txt", "preserve")
        target = self.skill / "assets/templates/NOW.md"
        before = target.read_bytes()
        errors, _, _ = bundle(self.root, check=True)
        for phrase in ("Unexpected", "Stale asset: assets/templates/NOW.md", "Missing asset: assets/templates/NEW.md"):
            self.assertTrue(any(phrase in e for e in errors), errors)
        self.assertEqual(target.read_bytes(), before)
        self.assertEqual(extra.read_text(), "preserve")
        self.assertFalse((self.skill / "assets/templates/NEW.md").exists())

    def test_rename_updates_expected_outputs_and_preserves_obsolete_copy(self):
        self.seed_assets()
        (self.root / "starter-kit/templates/RUNBOOK.md").rename(self.root / "starter-kit/templates/RENAMED.md")
        self.write("starter-kit/NOW.md", "# Changed\n")
        with redirect_stdout(io.StringIO()):
            errors, _, _ = bundle(self.root)
        self.assertTrue(any("RUNBOOK.md" in e and "preserved" in e for e in errors), errors)
        self.assertTrue((self.skill / "assets/templates/templates/RENAMED.md").is_file())
        self.assertTrue((self.skill / "assets/templates/templates/RUNBOOK.md").is_file())
        self.assertEqual((self.skill / "assets/templates/NOW.md").read_text(), "# Changed\n")

    def test_directory_at_output_reports_conflict_and_other_drift(self):
        self.seed_assets()
        target = self.skill / "assets/templates/NOW.md"
        target.unlink()
        target.mkdir()
        self.write("starter-kit/NEW.md", "# New\n")
        errors, _, _ = bundle(self.root, check=True)
        self.assertTrue(any("directory or symlink" in e for e in errors), errors)
        self.assertTrue(any("Missing asset" in e for e in errors), errors)
        self.assertTrue(target.is_dir())

    def test_file_blocking_directory_is_clear_and_preserved(self):
        self.seed_assets()
        templates = self.skill / "assets/templates/templates"
        shutil.rmtree(templates)
        templates.write_text("preserve", encoding="utf-8")
        with redirect_stdout(io.StringIO()):
            errors, _, _ = bundle(self.root)
        self.assertTrue(any("Expected a directory" in e for e in errors), errors)
        self.assertEqual(templates.read_text(), "preserve")

    def test_symlink_parent_is_rejected_before_writes(self):
        self.seed_assets()
        shutil.rmtree(self.root / "skills")
        outside = self.root / "outside"
        outside.mkdir()
        (self.root / "skills").symlink_to(outside, target_is_directory=True)
        errors, _, _ = bundle(self.root)
        self.assertTrue(any("Symlink directory" in e for e in errors), errors)
        self.assertEqual(list(outside.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
