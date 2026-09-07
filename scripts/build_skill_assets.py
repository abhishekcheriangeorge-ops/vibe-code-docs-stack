#!/usr/bin/env python3
"""Bundle canonical templates and the MIT notice into the portable skill; --check detects drift."""

import argparse
from pathlib import Path
import sys


def bundle(repo, check=False):
    """Update expected files without deleting extras; return all detected problems."""
    repo = Path(repo).resolve()
    source = repo / "starter-kit"
    skill = repo / "skills" / "vibe-code-docs-stack"
    target = skill / "assets" / "templates"
    license_source = repo / "LICENSE"
    license_target = skill / "LICENSE"
    problems = []
    for folder in (source, skill.parent, skill, target.parent, target):
        if folder.is_symlink():
            problems.append(f"Symlink directory is not supported: {folder.relative_to(repo)}")
        elif folder.exists() and not folder.is_dir():
            problems.append(f"Expected a directory: {folder.relative_to(repo)}")
    if not source.is_dir():
        problems.append("Canonical template directory is missing: starter-kit")
    # Never traverse a symlink while inspecting or writing the generated tree.
    if problems:
        return problems, 0, 0
    for folder in (source, target):
        for path in folder.rglob("*"):
            if path.is_symlink():
                problems.append(f"Symlink is not supported: {path.relative_to(repo)}")
    if problems:
        return problems, 0, 0

    expected = {p.relative_to(source): p for p in source.rglob("*.md")
                if p.is_file() and p.name != "ADOPTING-THIS-KIT.md"}
    if not expected:
        problems.append("No canonical templates found in starter-kit")
    if license_source.is_symlink() or not license_source.is_file():
        problems.append("The canonical LICENSE must be a regular file")
    present = {p.relative_to(target) for p in target.rglob("*") if p.is_file()}
    extras = sorted(present - expected.keys())
    if extras:
        problems.append("Unexpected generated assets (preserved): " + ", ".join(map(str, extras))
                        + ". Review deletions/renames, remove only obsolete generated copies, then rerun.")
    bundled = {target / relative: path for relative, path in expected.items()}
    if license_source.is_file() and not license_source.is_symlink():
        bundled[license_target] = license_source
    changed = 0
    for out, path in sorted(bundled.items()):
        label = out.relative_to(skill)
        if out.is_symlink() or (out.exists() and not out.is_file()):
            problems.append(f"Expected a regular file, found directory or symlink: {label} (preserved)")
            continue
        blocked = next((p for p in out.parents if p != repo and repo in p.parents
                        and p.exists() and not p.is_dir()), None)
        if blocked:
            problems.append(f"Expected a directory: {blocked.relative_to(repo)}; cannot write {label}")
            continue
        try:
            content = path.read_bytes()
            if out.is_file() and out.read_bytes() == content:
                continue
            changed += 1
            if check:
                state = "Stale" if out.exists() else "Missing"
                problems.append(f"{state} asset: {label}")
            else:
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_bytes(content)
                print(f"Updated: {label}")
        except OSError as error:
            problems.append(f"Cannot bundle {label}: {error.strerror}")
    return problems, len(expected), changed


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Report all drift without writing")
    args = parser.parse_args(argv)
    problems, count, changed = bundle(Path(__file__).resolve().parents[1], args.check)
    for problem in problems:
        print(problem, file=sys.stderr)
    print(f"{'Checked' if args.check else 'Bundled'} {count} templates and LICENSE; "
          f"{changed} {'differences' if args.check else 'updates attempted'}; {len(problems)} problems.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
