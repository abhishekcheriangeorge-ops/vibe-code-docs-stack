# Contributing

Keep the stack useful for a solo builder and a future teammate. Prefer a clear sentence, example, or reading path over another required document.

Use GitHub issues for a reproducible problem or suggestion, and pull requests against main for changes. Describe the practical problem and resulting improvement; no response time is promised. Coding agents also read the repository-specific boundaries in [AGENTS.md](AGENTS.md).

## Good changes

- Clarify an instruction that was difficult to follow in a real project.
- Correct provider behavior with a current primary source.
- Improve an existing template's ability to preserve intent, evidence, or ownership.
- Remove duplication or unnecessary maintenance.

## Before submitting

1. Explain the practical problem and resulting improvement.
2. Keep repository links relative and run the checks below.
3. Label examples and placeholders so they cannot be mistaken for verified project facts.
4. Keep tool-independent instructions in the shared contract and necessary adapters small.
5. Update related prompts and explanations when a template's responsibilities change.
6. Review public changes for credentials, sensitive logs, customer data, private project details, private contact details, personal conversation extracts, and local filesystem paths. Keep scratch drafts and isolated experiments under ignored work/; do not link to them from published files.

The CI here checks this toolkit. Templates do not configure CI, hosting, backups, or other infrastructure in an adopter's application. Keep provider claims grounded in current primary sources and distinguish the kit's recommendations from provider requirements.

## Source ownership

| Responsibility | Canonical source and related material |
|---|---|
| Workflow reasoning and document responsibilities | [Playbook](documentation-playbook.md); keep the README overview, public prompts, and skill document map consistent when responsibilities change |
| Portable agent workflow | [SKILL.md](skills/vibe-code-docs-stack/SKILL.md) and its references; reflect user-facing behavior changes in the public prompts where applicable |
| Adoptable document shapes | starter-kit; generated copies under skills/vibe-code-docs-stack/assets/templates must match |
| Installation and distribution | [INSTALL-SKILL.md](INSTALL-SKILL.md) |
| Maintainer rules and checks | This document; root AGENTS.md adds agent orientation and sample-file boundaries |

Update affected relationships rather than rewriting every file. Preserve historical decisions and label examples and target-project placeholders clearly.

## Checks

Use Python 3.10 or newer. Create a local environment once and install the pinned maintainer dependencies:

```sh
python3 -m venv work/checks-venv
work/checks-venv/bin/python -m pip install -r scripts/requirements-checks.txt
```

Then run from the repository root:

```sh
work/checks-venv/bin/python -B scripts/build_skill_assets.py --check
work/checks-venv/bin/python -B scripts/check_docs.py
work/checks-venv/bin/python -B -m unittest discover -s scripts/tests -v
```

On Windows, use work/checks-venv/Scripts/python.exe. In an already configured environment, substitute its python executable. Dependency installation needs package-index access; all three checks themselves run offline. The asset helper and tests use the standard library; the documentation checker uses markdown-it-py for CommonMark/table parsing and PyYAML for safe YAML parsing, with duplicate-key rejection. These dependencies are for maintainers; the installed skill has none.

The documentation checker verifies rendered local Markdown/image/reference links, HTML href/src links and explicit anchors, ordinary GitHub-style heading anchors (including duplicates), code line anchors, closing code fences, and standalone CLAUDE @file imports. It also checks portable frontmatter fields, this package's version/MIT fields, basic optional OpenAI interface metadata, symlinks, and links escaping the installed skill. Use explicit HTML anchors for unusual heading syntax. It skips external URLs and scratch/tool directories; plain-text file mentions, conditional template paths, Mermaid syntax, provider claims, and actual harness discovery still need relevant human or behavioral review. It is a repository validator, not a complete certification for every harness.

For a detached package, keep the final directory name vibe-code-docs-stack and run the same checker from the toolkit:

```sh
work/checks-venv/bin/python -B scripts/check_docs.py --skill /path/to/vibe-code-docs-stack
```

The [GitHub Actions workflow](.github/workflows/check.yml) runs the checks on pushes and pull requests with read-only repository permissions and no stored checkout credentials. It does not schedule external link checks or publish anything. Report checks as passed, failed, or not run, with scope and important limitations; do not claim a hosted workflow ran merely because its configuration exists.

## Skill changes

Keep skills/vibe-code-docs-stack self-contained and its entrypoint concise. Add mode-specific guidance in references only where it changes the agent's decisions. Use portable frontmatter in SKILL.md; optional Codex UI metadata belongs in agents/openai.yaml.

Edit canonical templates under starter-kit, then run `python3 scripts/build_skill_assets.py` and the checks above. Include generated assets with their source changes. On template deletion or rename, the helper reports and preserves obsolete generated files: review the listed paths, remove only the obsolete copies, then rerun. Generation still updates safe expected files, but exits unsuccessfully while extras or conflicts remain. Check mode reports all detected stale/missing/extra files without writing; no mode prunes files automatically. A file/directory conflict must be resolved deliberately before rerunning.

For meaningful behavioral changes, exercise a representative task in an isolated fixture and report what it demonstrated without claiming live testing in other harnesses. The local validator is shipped in this repository; external Skill Creator or skills-ref validators are optional additional tools and are not bundled here.

The root LICENSE is the canonical MIT notice. The same helper bundles and checks its standalone skill copy; regenerate that copy if the root notice changes.

## Releases

When publishing changes to skill instructions, references, or assets, bump metadata.version in SKILL.md and update [CHANGELOG.md](CHANGELOG.md), [SKILL-VALIDATION.md](SKILL-VALIDATION.md), the README release/quickstart, installation examples, and the adoption guide's version. Keep the tested scope explicit; do not relabel an earlier behavioral exercise as a new run.

Run the checks above and any representative exercise warranted by the behavior change. Commit the reviewed files, then tag that exact commit `vX.Y.Z` when publication is authorized. Publish the tag after the commit's CI passes. Release assets must be built from that tag and include the skill's full directory, hidden templates, and LICENSE. Preserve existing release tags; a correction gets a new version. Point adopters to tags; main may contain changes since the latest release.
