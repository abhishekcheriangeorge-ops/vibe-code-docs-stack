# Document map and template selection

Keep equivalent existing paths. In a new stack, use these destinations. Each template is a shape to adapt; inspect it only when producing that document. Core documents may be a few paragraphs. Add conditional documents when their responsibility applies, not merely because the asset exists.

| Canonical destination | Responsibility and trigger | Bundled template |
|---|---|---|
| README.md | Core: purpose, owner, entry points, audience reading paths | [README](../assets/templates/README.md) |
| NOW.md | Core: current objective, work location, state, next action | [NOW](../assets/templates/NOW.md) |
| AGENTS.md or existing equivalent | Core: short working and documentation contract | [AGENTS](../assets/templates/AGENTS.md) |
| docs/PRODUCT.md | Core: problem, users, accepted scope, domain rules, assumptions | [PRODUCT](../assets/templates/docs/PRODUCT.md) |
| docs/ARCHITECTURE.md | Core once a design exists: boundaries, core flow, code map, rationale, limits | [ARCHITECTURE](../assets/templates/docs/ARCHITECTURE.md) |
| docs/RISKS.md | Core: material defects, compromises, assumptions, verification gaps | [RISKS](../assets/templates/docs/RISKS.md) |
| docs/ENGINEERING.md | Once runnable: actual setup, commands, development and validation | [ENGINEERING](../assets/templates/docs/ENGINEERING.md) |
| docs/DATA.md | Once persistent: schema authority, meaning, access, lifecycle, contracts | [DATA](../assets/templates/docs/DATA.md) |
| docs/OPERATIONS.md | Once hosted/administered: ownership, environments, admin tasks, releases, diagnosis, recovery | [OPERATIONS](../assets/templates/docs/OPERATIONS.md) |
| docs/USER-GUIDE.md | Before others use it: actual tasks and first useful outcome | [USER GUIDE](../assets/templates/docs/USER-GUIDE.md) |

Conditional supporting records:

- Use the [decision template](../assets/templates/templates/DECISION.md) for consequential choices. Include context, actual alternatives, rationale, consequences, status, evidence, and revisit trigger. Link superseded records; do not rewrite history.
- Use the [runbook template](../assets/templates/templates/RUNBOOK.md) when a procedure needs its own page. Include role, environment, prerequisites, steps, expected observations, verification, escalation, and last exercise evidence.
- Use the [handover template](../assets/templates/templates/HANDOVER.md) as a dated record of transfer scope and exercises, linked to current manuals.
- Adapt the [PR template](../assets/templates/.github/pull_request_template.md) only when the repository uses PRs and its template needs documentation-impact guidance.
- The [Claude adapter](../assets/templates/CLAUDE.md) imports AGENTS.md for relevant Claude Code projects. Preserve existing instructions.
- The [portfolio template](../assets/templates/templates/PORTFOLIO.md) belongs in a private index across projects only when requested. Do not create a portfolio for every app.

## Canonical knowledge boundaries

PRODUCT describes intent. ARCHITECTURE describes the observed design and links to decision rationale. RISKS explains exposure and uncertainty. An issue tracker owns implementation task state; NOW points to current work. OPERATIONS owns live service procedures and account/configuration references. USER-GUIDE describes user-facing tasks without unnecessary implementation details.

For each material risk, record category, triggering condition, impact, evidence/confidence, workaround and limits, owner, and next action or revisit trigger. Distinguish a confirmed defect from a suspicion and a measured limit from untested capacity.

Diagram only what helps: a small context/container map, actual data relationships, and a sequence for a flow whose ordering matters. Label proposed components. Link source files rather than copying long generated reference material.
