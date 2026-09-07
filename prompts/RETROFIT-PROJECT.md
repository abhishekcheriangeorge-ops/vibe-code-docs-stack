# Retrofit an existing project

Open the existing project in your coding tool. Paste the prompt below and provide relevant planning notes, proposals, or conversation extracts if available. The templates in this repository can be supplied as references.

---

This is an existing project. Retrofit its documentation so I can return after a break, move between coding tools, and eventually hand it to engineers and operators.

First inspect the code, existing instructions and docs, tests, configuration, migrations, and relevant Git history. Inspect deployment information if accessible. Use evidence to distinguish what is implemented, tested, and deployed. Mark inaccessible or unverified information explicitly.

Establish:

- What the application actually does, who it serves, and what is known about its purpose.
- How its main workflows, components, dependencies, and data access work.
- Known defects, deliberate shortcuts, missing tests, operational gaps, and uncertain assumptions.
- How someone develops, administers, deploys, maintains, and recovers it.

Create or improve the following canonical documents, keeping them as short as their purpose allows:

- README.md: entry point, owner, useful links, and reading paths.
- NOW.md: current objective, actual implementation/test/deployment state, branch and work location, local-only changes, blockers, and next action.
- AGENTS.md: concise project-specific instructions, reading order, important constraints, links to real commands, and documentation maintenance rules.
- docs/PRODUCT.md: purpose, users, success criteria, scope/non-goals, domain rules, accepted decisions, and open assumptions.
- docs/ARCHITECTURE.md: current system map, core runtime flow, component-to-code map, constraints, rationale, and measured versus assumed limits.
- docs/RISKS.md: discoverable problems and compromises with category, evidence, impact, workaround, owner, and next action or revisit trigger.
- docs/ENGINEERING.md when runnable: prerequisites, verified setup and test commands, safe test data, migration/development workflow, and common failures.
- docs/DATA.md when persistent data exists: authoritative schema/migration sources, applied-state verification, relationships, business meaning, ownership/access, lifecycle, and integration contracts.
- docs/OPERATIONS.md when hosted or administered: environment mappings, account and billing ownership, secure access routes, product administration, deployment, diagnosis, recovery, maintenance, and escalation.
- docs/USER-GUIDE.md when others use it: real user tasks, expected outcomes, common errors, and help.

Preserve useful existing documentation and equivalent filenames. Give each fact one canonical home. Keep the existing issue tracker as the canonical backlog and link from docs instead of duplicating its task lists.

Do not invent historical reasoning from code or Git messages. Mark inferred rationale and ask focused questions about consequential missing intent while completing independent work. Separate accepted decisions, proposals, assumptions, and unknowns. Treat old planning material as historical and compare implementation claims with the current repository.

Record significant confirmed design decisions under docs/decisions/ with context, alternatives actually considered, reasons, consequences, status, and reconsideration triggers. Preserve superseded decisions and link their replacements. Include small diagrams only where they improve understanding.

Operations must cover product administrators and technical operators according to their actual responsibilities. Procedures need the required role, target environment, prerequisites, steps, expected result, verification, escalation, and last exercised evidence. Distinguish application rollback, database recovery, and object/file recovery. Label untested recovery explicitly.

Keep secrets, private customer data, sensitive logs, and credential-bearing URLs out of docs. Record configuration names and secure access locations. Use a private companion document for internal details when the repository is public.

For this pass, make documentation changes only. Record application fixes as follow-up work. Documentation work does not itself authorize production deployment, migrations, account changes, infrastructure deletion, or external messages.

Add a maintenance contract to the agent instructions:

1. Read NOW.md and relevant docs, then inspect actual Git state at the start of work.
2. Update affected canonical docs alongside meaningful changes to behavior, architecture, schema/access, setup/tests, or operations.
3. Record new problems and uncertainty with evidence in RISKS.md.
4. Update NOW.md at meaningful checkpoints and before handover, including what is committed/pushed versus local-only and the first next action.
5. Record checks as passed, failed, or not run, with scope and evidence. A changed date alone is not verification.

Keep tool-specific adapters small. If Claude Code is used, adapt CLAUDE.md to import the shared @AGENTS.md contract while preserving relevant existing rules. Verify each harness's instruction loading instead of assuming all Markdown is automatically read.

Finish by showing me:

1. A plain-language explanation of the current system.
2. The most important problems and unknowns, with evidence.
3. Questions only I can answer about intent or past choices.
4. The reading path for an engineer and an operator.
5. What was verified and the first concrete next action.

---

## For paused projects

Begin with purpose, current state, work location, known problems, what still runs or costs money, the responsible owner, and how to resume. Expand engineering and operational procedures when the project is reactivated or handed over.
