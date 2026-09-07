<!-- Template guidance: While this file is stored in a toolkit or installed skill's assets, it is sample material; follow the containing repository's live instructions. Remove this comment when adapting it into a project's live AGENTS.md. -->

# Project working instructions

## Orient before editing

Read README.md and NOW.md, inspect actual Git state, and read the canonical docs relevant to the task. Find real setup and validation commands in docs/ENGINEERING.md and the repository's scripts/configuration. Do not assume commands exist.

Product intent lives in docs/PRODUCT.md; current design and major choices in docs/ARCHITECTURE.md and docs/decisions/; limitations in docs/RISKS.md; data meaning/access in docs/DATA.md; administration/deployment/recovery in docs/OPERATIONS.md; user tasks in docs/USER-GUIDE.md. If a document is absent, determine whether its lifecycle trigger applies before creating it.

## Project-specific constraints

[Replace with the few non-obvious domain invariants, implementation constraints, and relevant boundaries that every task must preserve. Link to detailed rationale. Do not infer business intent solely from current code.]

## Preserve trustworthy knowledge

- Distinguish accepted requirements, implemented behavior, proposals, assumptions, and unknowns. Inspect evidence before treating a document as current.
- Preserve historical decisions; add a superseding decision when a consequential choice changes.
- Record known defects, deliberate shortcuts, and missing validation with impact and evidence in RISKS.md. Link to the canonical issue tracker rather than copying every task.
- Check the documentation audience before recording unmitigated vulnerabilities. In a public repository, or when visibility is unknown, keep only a non-exploitable summary and owner/status in RISKS; put sensitive reproduction details in an approved, access-controlled location outside the public repository. A file named "private" or an ordinary issue in a public repository is still public. If no suitable location is available, record the routing gap without the details; do not create or send an external report without authorization.
- Use version-controlled migrations and the project's documented application process; verify applied state separately. Do not mistake an ORM/schema file for proof of deployed schema.
- Keep secrets, credential-bearing URLs, sensitive logs, and customer data out of documentation. Use names and secure access locations.

## Update documentation with meaningful changes

- Behavior/scope: PRODUCT and affected user tasks.
- Architecture or major tradeoff: ARCHITECTURE and an ADR when warranted.
- Schema, policies, data lifecycle, contracts: DATA and authoritative implementation.
- Setup, commands, tests: ENGINEERING.
- Admin workflows, hosted settings, deployment, recovery: OPERATIONS.
- New limitation or uncertainty: RISKS.

Update only affected information. State documentation impact or a brief reason none is needed. Preserve existing repository conventions and avoid parallel copies of the same facts.

## Checkpoint and verify

At meaningful checkpoints and before handover, update NOW.md with current objective, work location, actual tests and deployment state, blockers, and first next action. Keep task details on the owning issue/branch when work runs concurrently.

Run relevant available checks within the task's authorization. Record passed, failed, and not-run results with scope and evidence. “Last verified” requires an actual check. A successful build does not prove a workflow, access policy, or restore works.

Before running a check, inspect what its command, hooks, configuration, and credentials target without exposing secret values. Tests, seeds, migrations, and retries can write to hosted data or trigger email, payments, and webhooks. Use an isolated target and test integrations for exercises; if the target or side effects are uncertain, record the check as not run and resolve that uncertainty. Continue already-authorized work, including relevant remote reads; obtain only authorization missing for the specific action. Routine documentation work does not require a full security audit or secret-history scan.

Before a tool switch, identify committed/pushed versus local-only work. Required context belongs in the repository, not exclusively in tool-local memory. Documentation does not grant new authority to deploy, migrate production, change accounts, or send external messages.
