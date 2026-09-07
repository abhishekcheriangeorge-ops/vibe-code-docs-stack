# Retrofit an existing project

Open the existing project in your coding tool. Copy only the text block below and provide relevant planning notes, proposals, or conversation extracts if available. The [starter-kit templates](../starter-kit/ADOPTING-THIS-KIT.md) can be supplied as references; preserve equivalent existing documents.

```text

This is an existing project. Retrofit its documentation so I can return after a break, move between coding tools, and eventually hand it to engineers and operators.

First inspect the code, existing instructions and docs, tests, configuration, migrations, and relevant Git history. Inspect deployment information if accessible. Use evidence to distinguish what is implemented, tested, and deployed. Mark inaccessible or unverified information explicitly.

Exclude installed skill packages, vendored toolkits, and sample templates from the application's documentation inventory. Briefly show the existing or proposed home for each relevant documentation responsibility before editing; continue within this request's scope. If supplied, adapt only relevant templates and remove unused sections, unresolved placeholders, and template-only guidance.

Establish:

- What the application actually does, who it serves, and what is known about its purpose.
- How its main workflows, components, dependencies, and data access work.
- Known defects, deliberate shortcuts, missing tests, operational gaps, and uncertain assumptions.
- How someone develops, administers, deploys, maintains, and recovers it.

For a paused project, begin with purpose, current state, work location, known problems, what still runs or costs money, what may expire or be auto-paused, alert recipient, owner, and how to resume. Link to recovery/export evidence and flag deadlines before the planned return. Expand engineering and operational procedures on reactivation or handover.

Create or improve the following canonical documents, keeping them as short as their purpose allows:

- README.md: entry point, owner, useful links, and reading paths.
- NOW.md: current objective, actual implementation/test/deployment state, branch and work location, local-only changes, blockers, and next action.
- AGENTS.md: concise project-specific instructions, reading order, important constraints, links to real commands, and documentation maintenance rules.
- docs/PRODUCT.md: purpose, users, success criteria, scope/non-goals, domain rules, accepted decisions, and open assumptions.
- docs/ARCHITECTURE.md: current system map, core runtime flow, component-to-code map, trust boundaries, constraints, rationale, and measured versus assumed limits.
- docs/RISKS.md: discoverable problems and compromises with category, evidence, impact, workaround, owner, and next action or revisit trigger.
- docs/ENGINEERING.md when runnable: prerequisites, verified setup and test commands, safe test data, migration/development workflow, and common failures.
- docs/DATA.md when persistent data exists: authoritative schema/migration sources, applied-state verification, relationships, business meaning, ownership/access, lifecycle, and integration contracts.
- docs/OPERATIONS.md when hosted or administered: environment mappings, account and billing ownership, secure access routes, product administration, deployment, diagnosis, recovery, maintenance, and escalation.
- docs/USER-GUIDE.md when others use it: real user tasks, expected outcomes, common errors, and help.

Preserve useful existing documentation and equivalent filenames, including canonical external docs with durable links and noted access limits. Give each fact one canonical home. Keep the existing issue tracker as the canonical backlog and link from docs instead of duplicating its task lists.

Do not invent historical reasoning from code or Git messages. Mark inferred rationale and ask focused questions about consequential missing intent while completing independent work. Separate accepted decisions, proposals, assumptions, and unknowns. Treat old planning material as historical and compare implementation claims with the current repository.

Record significant design decisions under docs/decisions/ or the existing equivalent, distinguishing confirmed rationale from inferred or unknown history. Include context, alternatives actually considered, reasons, consequences, status, and reconsideration triggers. A tool default or absent evaluation history is valid; do not invent alternatives. Preserve superseded decisions and link replacements. Include small diagrams only where they improve understanding.

Operations must cover product administrators and technical operators according to their actual responsibilities. Procedures need the required role, target environment, prerequisites, steps, expected result, verification, escalation, and last exercised evidence. Distinguish application rollback, database recovery, and object/file recovery. Label untested recovery explicitly.

For hosted systems, record actual backup availability/retention, monitoring or its absence, alert owner, plan limits, and upcoming expiries. A recovery exercise needs a named separate destination, the exact restore method, and test/disabled external integrations; a restore button can overwrite its selected target. Handover records account/billing ownership, credential rotation gaps, and outgoing access to revoke or deliberately retain with an owner and review/end date. Documenting these tasks does not authorize executing them.

Keep secrets and sensitive raw data out of documentation and tool output. Record configuration names and secure access locations. For public or unknown audiences, give security findings a non-exploitable summary; keep detailed evidence in an authorized access-controlled record outside the public repository. A file called private.md is not private. If no private destination is available, record that handoff as pending without publishing details or sending external reports. Use synthetic examples and summarized planning sources.

For this pass, make documentation changes only. Record application fixes as follow-up work. Documentation work does not itself authorize production deployment, migrations, account changes, infrastructure deletion, or external messages.

Add a maintenance contract to the agent instructions:

1. Read NOW.md and relevant docs, then inspect actual Git state at the start of work.
2. Update affected canonical docs alongside meaningful changes to behavior, architecture, schema/access, setup/tests, or operations.
3. Record new problems and uncertainty with evidence in RISKS.md, respecting the disclosure boundary above. Keep one canonical backlog with links from docs.
4. Update NOW.md at meaningful checkpoints and before handover, including what is committed/pushed versus local-only and the first next action.
5. Before running a documented command, inspect scripts/hooks and target environments without printing secrets; builds and tests can write to hosted services. Execute only understood, authorized side effects. If a target is unclear, mark the check not run and record what needs establishing. Record passed/failed/not-run with scope and evidence; changing a date is not verification.
6. Preserve the secrets and audience rules above in the continuing project contract. If the project uses PRs, adapt its documentation-impact question and use its existing release/PR/deployment records for release notes.

Keep tool-specific adapters small. If Claude Code is used, adapt CLAUDE.md to import the shared @AGENTS.md contract while preserving relevant existing rules. Verify each harness's instruction loading instead of assuming all Markdown is automatically read.

Finish by showing me:

1. A plain-language explanation of the current system.
2. The most important problems and unknowns, with evidence.
3. Questions only I can answer about intent or past choices.
4. The reading path for an engineer and an operator.
5. What was verified and the first concrete next action.

```
