# Contributing

Keep the stack useful for a solo builder and a future teammate. Prefer a clear sentence, example, or reading path over another required document.

## Good changes

- Clarify an instruction that was difficult to follow in a real project.
- Correct provider behavior with a current primary source.
- Improve an existing template's ability to preserve intent, evidence, or ownership.
- Remove duplication or unnecessary maintenance.

## Before submitting

1. Explain the practical problem and resulting improvement.
2. Keep links relative for repository files and check that targets exist.
3. Label examples and placeholders so they cannot be mistaken for verified project facts.
4. Keep tool-independent instructions in the shared contract and necessary adapters small.
5. Update related prompts and explanations when a template's responsibilities change.
6. Include no private project details, credentials, or personal conversation extracts.

This repository contains guidance and templates. A change to a document should not imply that CI, hosting, backups, or other infrastructure has been configured.

## Skill changes

Keep skills/vibe-code-docs-stack self-contained and its entrypoint concise. Add mode-specific guidance in references only where it changes the agent's decisions. Use portable frontmatter in SKILL.md; optional Codex UI metadata belongs in agents/openai.yaml.

Edit canonical templates under starter-kit, then run `python3 scripts/build_skill_assets.py` and `python3 scripts/build_skill_assets.py --check`. Commit the resulting assets with their sources. Check links within a detached copy of the skill. For meaningful behavioral changes, exercise a representative task in an isolated fixture and report what it demonstrated without claiming live testing in other harnesses.

The root LICENSE is the canonical MIT notice. The same helper bundles and checks its standalone skill copy; regenerate that copy if the root notice changes.
