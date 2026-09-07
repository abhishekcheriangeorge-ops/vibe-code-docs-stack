#!/usr/bin/env python3
"""Bundle canonical starter-kit templates into the portable skill; --check detects drift."""

import argparse
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Report stale/missing/extra assets without writing")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    source = repo / "starter-kit"
    target = repo / "skills" / "vibe-code-docs-stack" / "assets" / "templates"
    expected = {
        p.relative_to(source): p
        for p in source.rglob("*.md")
        if p.name != "ADOPTING-THIS-KIT.md"
    }
    if not expected:
        parser.error("No canonical templates found in starter-kit")
    if any(p.is_symlink() for p in source.rglob("*")):
        parser.error("Canonical templates must be regular files and directories")
    if target.is_symlink() or any(p.is_symlink() for p in target.parents if p != repo.parent):
        parser.error("The generated destination must not traverse a symlink")
    if target.exists() and any(p.is_symlink() for p in target.rglob("*")):
        parser.error("The generated destination must not contain symlinks")
    present = {p.relative_to(target) for p in target.rglob("*") if p.is_file()} if target.exists() else set()
    extras = present - expected.keys()
    if extras:
        print("Unexpected generated assets; review before removing: " + ", ".join(map(str, sorted(extras))), file=sys.stderr)
        return 1
    changed = []
    for relative, path in sorted(expected.items()):
        out = target / relative
        content = path.read_bytes()
        if not out.is_file() or out.read_bytes() != content:
            changed.append(relative)
            if not args.check:
                out.parent.mkdir(parents=True, exist_ok=True)
                out.write_bytes(content)
    if args.check and changed:
        print("Stale or missing assets: " + ", ".join(map(str, changed)), file=sys.stderr)
        return 1
    print(f"{'Checked' if args.check else 'Bundled'} {len(expected)} templates; {len(changed)} {'differences' if args.check else 'updated'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
