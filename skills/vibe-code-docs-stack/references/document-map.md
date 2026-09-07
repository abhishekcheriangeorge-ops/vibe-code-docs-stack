# Document map and template selection

Keep equivalent existing paths. In a new stack, use these destinations. Each template is a shape to adapt; inspect it only when producing that document. Core documents may be a few paragraphs. Add conditional documents when their responsibility applies, not merely because the asset exists.

Replace adopted placeholders with facts, actionable unknowns, or a justified not-applicable; remove unused sections and template-only guidance. Keep useful ongoing maintenance instructions. The [fictional examples](examples.md) illustrate a short checkpoint, honest decision rationale, and a private-risk pointer when a concrete model would help.

When copying or adapting substantial portions of the bundled templates, retain the [MIT notice](../LICENSE) in the target's third-party notices or a file such as `LICENSES/vibe-code-docs-stack.txt`. Preserve the target application's existing license.

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

- Use the [decision template](../assets/templates/templates/DECISION.md) for consequential choices, in `docs/decisions/ADR-NNN-short-name.md` or the existing equivalent. Include context, actual alternatives, rationale, consequences, status, evidence, and revisit trigger. Link superseded records; do not rewrite history.
- Use the [runbook template](../assets/templates/templates/RUNBOOK.md) when a procedure needs its own page, in `docs/runbooks/task-name.md` or the existing equivalent. Include role, environment, prerequisites, steps, expected observations, verification, escalation, and last exercise evidence.
- Use the [handover template](../assets/templates/templates/HANDOVER.md) in `docs/handovers/YYYY-MM-DD-role.md` or the existing equivalent as a dated record of transfer scope and exercises, linked to current manuals.
- Adapt the [PR template](../assets/templates/.github/pull_request_template.md) only when the repository uses PRs and its template needs documentation-impact guidance.
- The [Claude adapter](../assets/templates/CLAUDE.md) imports AGENTS.md for relevant Claude Code projects. Preserve existing instructions.
- The [portfolio template](../assets/templates/templates/PORTFOLIO.md) belongs in a private index across projects only when requested. Do not create a portfolio for every app.

Use the existing release/PR/deployment record for release changes; do not introduce a parallel changelog in a target project unless it needs one. Link only records/directories actually adopted, and adapt instruction-file paths accordingly.

## Disclosure boundary

Establish the documentation audience from available evidence. For public or unknown visibility, describe exploitable security findings only at a level that does not expose reproduction steps, affected secret values, or attack-enabling implementation details. Keep the detailed evidence in an authorized access-controlled record outside the public repository; naming a file `private.md` or ignoring it in Git does not establish access control. If no such destination is available, record the private-detail handoff as pending without publishing the details. Do not create or send an external report unless authorized. Use synthetic examples instead of customer records, and summarize private planning sources without copying sensitive extracts.

## Canonical knowledge boundaries

PRODUCT describes intent. ARCHITECTURE describes the observed design and links to decision rationale. RISKS explains exposure and uncertainty. An issue tracker owns implementation task state; NOW points to current work. OPERATIONS owns live service procedures and account/configuration references. USER-GUIDE describes user-facing tasks without unnecessary implementation details.

For each material risk, record category, triggering condition, impact, evidence/confidence, workaround and limits, owner, and next action or revisit trigger. Distinguish a confirmed defect from a suspicion and a measured limit from untested capacity.

Diagram only what helps: a small context/container map, actual data relationships, and a sequence for a flow whose ordering matters. Label proposed components. Link source files rather than copying long generated reference material.
