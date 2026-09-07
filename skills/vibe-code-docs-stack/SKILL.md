---
name: vibe-code-docs-stack
description: Create, retrofit, or maintain repository documentation that preserves product intent, design decisions, known risks, current work state, and engineer/operator handovers. Use for documentation-stack setup, documentation updates after code changes, project checkpoints, and handover preparation. For ordinary coding tasks, use only when documentation work is requested or required by the project's existing instructions.
license: MIT
metadata:
  version: "0.1.1"
---

# Vibe Code Docs Stack

Give a returning builder, incoming engineer, or operator enough context to understand the project and continue their work. Maintain one canonical home for each fact. The target repository holds project knowledge; this skill holds the reusable workflow.

## Select the requested scope

Infer the mode from the request; these labels are ordinary task words, not a command parser.

| Need | Mode and reference |
|---|---|
| Start documentation for a new project | Bootstrap: [setup guidance](references/setup.md) |
| Recover documentation for existing code | Retrofit: [setup guidance](references/setup.md) |
| Bring docs into line with a specific change | Maintain: [maintenance guidance](references/maintenance.md) |
| Pause, resume, or switch harnesses | Checkpoint: [maintenance guidance](references/maintenance.md) |
| Prepare engineer or operator transfer | Handover: [handover guidance](references/handover.md) |

For a read-only review, report gaps and recommended changes without modifying files. A narrow request to update one document remains narrow; do not turn it into a full retrofit.

## Establish the target and evidence

Use the repository the user is working on, not this installed skill directory. Read its applicable instructions, current-state document, and task-relevant implementation before editing. Identify equivalent existing documents and preserve their useful names, content, and conventions. If the target is ambiguous, clarify it before writing.

Distinguish accepted intent, current implementation, proposed work, inferred historical rationale, and unknowns. Code shows implementation; it cannot establish why a founder chose it. Route consequential unanswered questions to the owner while completing independent work. Treat old proposals as dated sources, not automatic instructions.

Inspect only evidence relevant to the requested scope. If deployment, database, or account information is inaccessible, record what remains unknown. Distinguish implemented, tested, and deployed. Keep changes to application code and external systems within the user's actual authorization; documentation work does not authorize operational changes.

## Choose and adapt documents

Consult the [document map](references/document-map.md) to select canonical destinations and bundled templates. Read only the assets needed for this task. All references resolve within this skill package. Template filenames are defaults, not a migration requirement.

Fill adopted sections with project-specific facts or actionable unknowns. Use short evidence-backed descriptions and link to real code, tests, issues, or deployment records. Avoid copying an entire empty scaffold. Preserve important design decisions and their consequences; record why a shortcut was accepted and what would trigger reconsideration.

Keep repetitive schema/API details derived from the actual source where generation exists. Explain business meaning, access, lifecycle, and limitations in prose. Do not invent a generator, supported command, user workflow, capacity claim, or recovery guarantee.

Keep credentials, sensitive logs, customer data, and private conversation extracts out of public docs. Record configuration names and access routes at the appropriate visibility. Preserve other contributors' work and use one canonical backlog with links from the docs.

## Leave a maintainable result

For bootstrap/retrofit, adapt a concise maintenance contract in the target's existing agent instructions, pointing to its actual document names. For subsequent work, honor that contract and update only affected information. Do not overwrite an existing AGENTS.md or CLAUDE.md wholesale, or create duplicate contracts in multiple harness files. Add a Claude import adapter only when Claude Code is relevant and compatible with existing instructions.

Check changed links and implementation references, plus relevant commands when safely runnable within scope. Record checks as passed, failed, or not run with their limits. A date changes to “last verified” only after an actual check.

Finish with a short orientation: where to start, what changed, what was verified, the consequential gaps or owner questions, and the first concrete next action. Report handover readiness by responsibility and evidence, rather than a blanket claim that the project is production-ready.
