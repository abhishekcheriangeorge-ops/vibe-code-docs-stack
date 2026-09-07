# Adopting this kit

These files are adaptable templates, not documentation of an audited application.

Use the [repo-link quickstart](../README.md#quick-start-give-this-to-your-coding-agent), the [new-project prompt](../START-PROJECT.md), or the [existing-project prompt](../prompts/RETROFIT-PROJECT.md). The [playbook](../documentation-playbook.md) explains the reasoning when needed. Copy only files appropriate to the project's stage, merging existing docs and instructions. Replace adopted placeholders with facts, actionable unknowns, or justified not-applicable statements; remove unused sections and template-only guidance.

When copying or adapting substantial portions of these templates, retain the toolkit's [MIT notice](../LICENSE) in your project's third-party notices or a file such as `LICENSES/vibe-code-docs-stack.txt`. Preserve your application's existing license; adopting the toolkit does not require changing it to MIT.

Begin with README, NOW, AGENTS, PRODUCT, ARCHITECTURE, and RISKS. Add ENGINEERING when runnable, DATA when persistent, OPERATIONS when hosted, and USER-GUIDE before others use the product. This kit includes later-stage files so you have their templates ready; their presence does not make your project ready for handover.

The decision, runbook, and handover files under templates/ are sources for documents you create when needed. The portfolio template belongs once in your private project index, rather than in every application repo.

Core files go at the project root; `docs/` files keep their relative paths. Record defaults are `docs/decisions/ADR-NNN-short-name.md`, `docs/runbooks/task-name.md`, and `docs/handovers/YYYY-MM-DD-role.md`; use existing equivalent locations when present. The PR template lives in the hidden `.github/` directory and is relevant only when the project uses PRs. Adapt links to the files actually created.

CLAUDE.md imports the common contract for Claude Code. Keep any necessary harness-specific additions small. Verify that your actual tools load the intended instructions. A Markdown instruction is guidance, not an enforcement mechanism.

No application commands, credentials, infrastructure, CI workflow, or account integrations have been configured by this kit. Adapt the PR template to the repository's actual workflow.

## Updating an adopted project

Record the [upstream repository](https://github.com/abhishekcheriangeorge-ops/vibe-code-docs-stack) and adopted tag or commit in existing project/tooling notes. This kit version is v0.2.0; review [CHANGELOG.md](../CHANGELOG.md) when returning to it. Apply relevant improvements to your completed docs while preserving their project facts; do not replace them with fresh templates.
