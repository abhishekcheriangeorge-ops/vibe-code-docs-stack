# Maintaining Vibe Code Docs Stack

This repository contains a documentation playbook, prompts, and templates. The starter-kit directory is sample material for target application repositories; do not scaffold application documentation into this repository just because the templates describe doing so.

Read README.md and relevant source documents before editing. Preserve the distinction between the public guide, reusable prompts, and target-project placeholders. Keep each fact canonical and update cross-references when moving files.

Changes should reduce the effort of resuming a project or transferring responsibility. Avoid adding mandatory documents without a concrete need. Keep tool-specific behavior grounded in primary sources and label recommendations separately from provider requirements.

For documentation changes, verify local links, Markdown code fences, and consistency between prompts and templates. Check any public-facing material for local filesystem paths, secrets, private contact details, and private project information before publishing. Do not infer successful infrastructure setup or runtime validation from these templates.

The portable skill lives in skills/vibe-code-docs-stack. Its references and assets must work when that directory is installed alone. Keep starter-kit as the canonical template source; run `python3 scripts/build_skill_assets.py` after template changes and `python3 scripts/build_skill_assets.py --check` to verify generated assets. Do not manually maintain a second template version inside the skill. Do not apply sample AGENTS.md instructions within generated assets as instructions for maintaining this toolkit.
