# Paste this into a coding agent at the start of a project

For a new project, copy only the setup text block below into the agent working in the target repository, with your project brief. A brief summarizes the problem, users, accepted scope, constraints, and next task; the planning prompt below can extract one. For existing code, prefer [the retrofit prompt](prompts/RETROFIT-PROJECT.md). Each later text block is a separate prompt for its named situation.

```text

Establish and maintain a concise, evidence-based documentation stack for this project. It must help me return after an interruption, move between coding tools, and eventually hand the system to expert engineers and operating teammates.

First inspect the repository, existing instructions, documentation, configuration, migrations, tests, and any planning material I supplied. Summarize the actual product and implementation. Preserve useful existing documents and map equivalent files to the responsibilities below. Consolidate conflicting duplication carefully; keep historical decisions discoverable. Do not generate generic claims of completeness, security, scalability, deployment, or test success.

Exclude installed skills, vendored toolkits, and sample templates from the application's documentation inventory. If toolkit templates are supplied, use only the relevant ones as references. Remove unused sections, unresolved template placeholders, and template-only guidance from finished docs.

Give each fact one canonical home. Distinguish accepted intent, current implementation, proposed work, inferred rationale, and unknowns. Code can establish implementation; it cannot establish why I chose it. Ask concise questions only about consequential missing intent that cannot be recovered from available material, while completing independent documentation work.

Create or adapt the six core documents, initially short:

- README.md: one-sentence purpose, owner, useful entry points, and reading paths for returning owner, engineer, operator, and user.
- NOW.md: current objective, implemented/tested/deployed state, work branch and tested code revision, active issue/PR, local versus pushed work, top blocker, and the next concrete action. Keep it to a screen or two, usually no more than 500 words; shorter is fine.
- AGENTS.md: concise shared instructions, reading order, key product/technical constraints, links to real commands and relevant docs, and the maintenance rules below.
- docs/PRODUCT.md: problem, intended users, desired outcome, scope and non-goals, domain rules, examples, accepted decisions, and unresolved product assumptions.
- docs/ARCHITECTURE.md: current system map, main runtime flow, component-to-code map, trust boundaries, constraints, rationale, and measured versus assumed limitations.
- docs/RISKS.md: discoverable known defects, deliberate shortcuts, unverified assumptions, operational gaps, and missing validation. Include evidence, impact, workaround, owner, and a next action or revisit trigger. Link to the canonical issue tracker.

Add these when applicable: docs/ENGINEERING.md once runnable; docs/DATA.md once persistent data exists; docs/OPERATIONS.md once hosted or administered; docs/USER-GUIDE.md before others use it. A small document is sufficient. Mark unknown facts explicitly. Do not create empty manuals or invent supported workflows.

Record each consequential choice in docs/decisions/ or an existing equivalent, with context, alternatives actually considered, rationale, consequences, status, and revisit trigger. Label reconstructed reasoning as inferred; a tool default or unknown evaluation history is valid and needs no invented alternatives. Preserve accepted decisions when superseded and link their replacements. Do not write an ADR for routine edits.

Operations must distinguish product administration from technical operations. Document real environment mappings, account/access ownership, configuration sources, billing/maintenance responsibilities, releases, diagnosis, application rollback, database and file recovery, and escalation as applicable. Each procedure needs target environment, prerequisites, steps, expected result, verification, and last exercised evidence. Unknown recovery remains explicitly unverified.

For hosted systems, record actual backup availability/retention, monitoring or its absence, alert owner, plan limits, and upcoming expiries. A recovery exercise needs a named separate destination, the exact restore method, and test/disabled external integrations; a restore button can overwrite its selected target. Handover records account/billing ownership, credential rotation gaps, and outgoing access to revoke or deliberately retain with an owner and review/end date. Documenting these tasks does not authorize executing them.

Use existing migrations/schema definitions as the intended schema source; document how their applied state is checked. Explain data semantics, ownership/access policies, and lifecycle. Generate repetitive schema/type/API reference only from real sources and identify the generator. Include a compact system diagram and important data relationships; add a sequence diagram only for a workflow whose ordering needs explanation.

For tool portability, keep common instructions in AGENTS.md. If Claude Code is used, create or adapt a small CLAUDE.md that imports @AGENTS.md without repeating the common rules. Preserve meaningful existing tool-specific instructions. Verify the receiving harness's entry-point behavior rather than assuming all Markdown loads automatically. Do not store required project context only in machine-local agent memory.

Maintenance contract for future work:

1. At the start, read the relevant project instructions and NOW.md, inspect actual Git state, and load documents needed for this task. Resolve discrepancies using evidence; do not silently rewrite product intent to match a bug.
2. With a meaningful code change, update affected canonical docs in the same change. Product behavior affects product/user docs; architecture affects architecture/decisions; schema/access affects data docs; setup/tests affect engineering; deployment/admin/recovery affects operations; discovered limitations affect risks.
3. If the repository uses PRs, adapt its PR template with a documentation-impact question, allowing “not affected” with a reason. Use its existing release/PR/deployment records for release notes.
4. At meaningful checkpoints and before a handover, update NOW.md with progress, actual validation, transferable work location, blockers, and next action. Do not claim a commit is pushed or deployed without checking.
5. Keep one canonical backlog, normally the existing issue tracker. Link from docs rather than maintaining duplicate task lists. Concurrent branches should keep task details in their own issue or branch note.
6. Keep secrets and sensitive raw data out of documentation and tool output. Record variable names and secure access locations. For public or unknown audiences, give security findings a non-exploitable summary; keep detailed evidence in an authorized access-controlled record outside the public repository. A file called private.md is not private. If no private destination is available, record that handoff as pending without publishing details or sending external reports. Use synthetic examples and summarized planning sources.
7. Verify links and implementation references. Before running a documented command, inspect scripts/hooks and target environments without printing secrets; builds and tests can write to hosted services. Execute only understood, authorized side effects. If a target is unclear, mark the check not run and record what needs establishing. Label checks passed/failed/not-run with scope and evidence; changing a date is not verification.

Apply documentation changes within this repository. This documentation task does not itself authorize production migrations, deployments, account changes, external messages, or infrastructure deletion.

Finish with the shortest useful summary: what this project does, where to start, what you verified, the main unresolved context/risk questions, and the next concrete action. Identify any operational capability that remains undocumented or untested. Treat readiness as demonstrated responsibilities rather than a blanket “production-ready” label.

```

## End a planning conversation with this

Paste this into the planning conversation, then pass the resulting brief to the coding agent.

```text
Extract a durable project brief from this conversation. Separate accepted decisions, proposals, assumptions, and unresolved questions. Preserve the user problem, success criteria, domain rules, important rejected alternatives and their reasons, constraints, deliberate shortcuts, and revisit triggers. Do not treat brainstorming as approval. Include provenance links or dated summaries where useful; keep secrets and private customer or personal details out of the shareable brief. Produce a compact brief the coding agent can reconcile against the repository, with the next implementation task and observable acceptance criteria.
```

## Resume or switch tools with this

```text
Read the project's instructions and NOW.md, inspect the actual branch and working tree, and open the canonical documents relevant to the current task. In a short orientation, state the product purpose, current objective, key constraints, most important limitation, actual validation/deployment state, and next action. Identify stale or contradictory information. Continue the already-authorized work once oriented; ask only if a consequential ambiguity blocks it.

When switching tools, identify the receiving instruction entry point and relevant scoped rules. Verify loading in the receiving session using its instruction view when available and by asking it to identify applicable files and maintenance obligations. If that session is unavailable, record discovery as unverified and leave the check as a next action. Confirm which work is transferable versus local-only.
```

## End a work session with this

```text
Create a durable checkpoint. Update affected canonical docs and NOW.md. State what changed, what was actually tested, what is deployed, what is committed/pushed versus local-only, unresolved issues, useful evidence from failed attempts, and the first concrete next action. Keep private data and secrets out. Preserve other contributors' work. Do not invent a successful check, commit, push, or deployment.
```
