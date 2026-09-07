# Paste this into a coding agent at the start of a project

Use this prompt in the actual target repository. Attach any planning proposal or relevant conversation extract. It works for new and existing projects; do not overwrite an existing documentation system just to match these filenames.

---

Establish and maintain a concise, evidence-based documentation stack for this project. It must help me return after an interruption, move between coding tools, and eventually hand the system to expert engineers and operating teammates.

First inspect the repository, existing instructions, documentation, configuration, migrations, tests, and any planning material I supplied. Summarize the actual product and implementation. Preserve useful existing documents and map equivalent files to the responsibilities below. Consolidate conflicting duplication carefully; keep historical decisions discoverable. Do not generate generic claims of completeness, security, scalability, deployment, or test success.

Give each fact one canonical home. Distinguish accepted intent, current implementation, proposed work, inferred rationale, and unknowns. Code can establish implementation; it cannot establish why I chose it. Ask concise questions only about consequential missing intent that cannot be recovered from available material, while completing independent documentation work.

Create or adapt the six core documents, initially short:

- README.md: one-sentence purpose, owner, useful entry points, and reading paths for returning owner, engineer, operator, and user.
- NOW.md: current objective, implemented/tested/deployed state, work branch and tested code revision, active issue/PR, local versus pushed work, top blocker, and the next concrete action. Keep it approximately 300–500 words.
- AGENTS.md: concise shared instructions, reading order, key product/technical constraints, links to real commands and relevant docs, and the maintenance rules below.
- docs/PRODUCT.md: problem, intended users, desired outcome, scope and non-goals, domain rules, examples, accepted decisions, and unresolved product assumptions.
- docs/ARCHITECTURE.md: current system map, main runtime flow, component-to-code map, trust boundaries, constraints, rationale, and measured versus assumed limitations.
- docs/RISKS.md: discoverable known defects, deliberate shortcuts, unverified assumptions, operational gaps, and missing validation. Include evidence, impact, workaround, owner, and a next action or revisit trigger. Link to the canonical issue tracker.

Add these when applicable: docs/ENGINEERING.md once runnable; docs/DATA.md once persistent data exists; docs/OPERATIONS.md once hosted or administered; docs/USER-GUIDE.md before others use it. A small document is sufficient. Mark unknown facts explicitly. Do not create empty manuals or invent supported workflows.

Record each consequential choice in docs/decisions/ with context, alternatives actually considered, rationale, consequences, status, and revisit trigger. Label reconstructed reasoning as inferred. Preserve accepted decisions when superseded and link their replacements. Do not write an ADR for routine edits.

Operations must distinguish product administration from technical operations. Document real environment mappings, account/access ownership, configuration sources, billing/maintenance responsibilities, releases, diagnosis, application rollback, database and file recovery, and escalation as applicable. Each procedure needs target environment, prerequisites, steps, expected result, verification, and last exercised evidence. Unknown recovery remains explicitly unverified.

Use existing migrations/schema definitions as the intended schema source; document how their applied state is checked. Explain data semantics, ownership/access policies, and lifecycle. Generate repetitive schema/type/API reference only from real sources and identify the generator. Include a compact system diagram and important data relationships; add a sequence diagram only for a workflow whose ordering needs explanation.

For tool portability, keep common instructions in AGENTS.md. If Claude Code is used, create or adapt a small CLAUDE.md that imports @AGENTS.md without repeating the common rules. Preserve meaningful existing tool-specific instructions. Verify the receiving harness's entry-point behavior rather than assuming all Markdown loads automatically. Do not store required project context only in machine-local agent memory.

Maintenance contract for future work:

1. At the start, read the relevant project instructions and NOW.md, inspect actual Git state, and load documents needed for this task. Resolve discrepancies using evidence; do not silently rewrite product intent to match a bug.
2. With a meaningful code change, update affected canonical docs in the same change. Product behavior affects product/user docs; architecture affects architecture/decisions; schema/access affects data docs; setup/tests affect engineering; deployment/admin/recovery affects operations; discovered limitations affect risks.
3. Add a short documentation-impact question to the existing PR template, allowing “not affected” with a reason. Use the repository's existing release mechanism for release notes.
4. At meaningful checkpoints and before a handover, update NOW.md with progress, actual validation, transferable work location, blockers, and next action. Do not claim a commit is pushed or deployed without checking.
5. Keep one canonical backlog, normally the existing issue tracker. Link from docs rather than maintaining duplicate task lists. Concurrent branches should keep task details in their own issue or branch note.
6. Never copy secrets, credential-bearing connection strings, customer data, or sensitive logs into docs. Record variable names and secure access locations. Respect public versus private documentation audiences.
7. Verify links, documented commands where safely runnable, and implementation references. Label checks as passed, failed, or not run, with scope and evidence. Updating a date alone does not constitute verification.

Apply documentation changes within this repository. This documentation task does not itself authorize production migrations, deployments, account changes, external messages, or infrastructure deletion.

Finish with the shortest useful summary: what this project does, where to start, what you verified, the main unresolved context/risk questions, and the next concrete action. Identify any operational capability that remains undocumented or untested. Treat readiness as demonstrated responsibilities rather than a blanket “production-ready” label.

---

## End a planning conversation with this

Extract a durable project brief from this conversation. Separate accepted decisions, proposals, assumptions, and unresolved questions. Preserve the user problem, success criteria, domain rules, important rejected alternatives and their reasons, constraints, deliberate shortcuts, and revisit triggers. Do not treat brainstorming as approval. Include provenance links or dated excerpts where useful. Produce a compact brief the coding agent can reconcile against the repository, with the next implementation task and observable acceptance criteria.

## Resume or switch tools with this

Read the project's instructions and NOW.md, inspect the actual branch and working tree, and open the canonical documents relevant to the current task. In a short orientation, state the product purpose, current objective, key constraints, most important limitation, actual validation/deployment state, and next action. Identify stale or contradictory information. Continue the already-authorized work once oriented; ask only if a consequential ambiguity blocks it.

## End a work session with this

Create a durable checkpoint. Update affected canonical docs and NOW.md. State what changed, what was actually tested, what is deployed, what is committed/pushed versus local-only, unresolved issues, useful evidence from failed attempts, and the first concrete next action. Keep private data and secrets out. Preserve other contributors' work. Do not invent a successful check, commit, push, or deployment.
