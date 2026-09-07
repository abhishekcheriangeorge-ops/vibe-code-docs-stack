# Bootstrap and retrofit

## Bootstrap

Extract accepted intent from the brief: intended user, problem, smallest useful outcome, scope/non-goals, domain invariants, and real constraints. Separate suggestions and unproven assumptions. Establish the small core stack using the document map. For an unbuilt system, label architecture as proposed and runnable/deployed behavior as absent or unknown.

Capture a next implementation task with observable acceptance criteria in NOW or the existing tracker. Create engineering, data, operations, and user documentation only as applicable. Do not fabricate future infrastructure to fill a template.

## Retrofit

Inventory existing docs, relevant implementation/configuration, tests, migrations, and available history. Exclude installed skill packages, vendored toolkits, and sample templates from the application's documentation inventory. Briefly state each responsibility's existing or proposed home before editing; this is an orientation, not a required approval gate. Preserve canonical external docs/backlogs when used, with durable repository links and access limitations. Resolve duplication with targeted consolidation and record unresolved contradictions.

Trace a core workflow from entry point through authorization, processing, persistence, and external effects where present. Record implementation locations and test evidence. Inspect hosted configuration only through available, authorized access. Local source does not prove the deployed environment matches it.

Recover intent from dated proposals, owner notes, or confirmed decisions. Record missing rationale as unknown or inferred, and ask only consequential questions that the evidence cannot answer. A proposal's detail or confidence does not make it accepted.

Prioritize information an incoming engineer cannot reconstruct cheaply: why the product exists, what must remain true, constraints behind major choices, deliberate shortcuts, where problems are, and what remains unverified. Record follow-up application work without performing it in a documentation-only task.

For a paused project, start with purpose, current state, work location, known problems, what still runs or may expire, owner, and resumption steps. Expand manuals when the project reactivates or transfers responsibility. Keep unanswered owner questions in their canonical document as well as the closing report.

## Environment and data coverage

When relevant, map application environments to actual database projects/branches, auth, storage, and external services. Record configuration names and secure access locations, including dashboard-only settings. Avoid assuming a preview frontend has an isolated backend.

Identify version-controlled schema sources and separately record how applied migration state is verified. Explain row ownership/access, sensitive fields, and data lifecycle. Distinguish database recovery from object/file recovery and application rollback. Document the project's actual retention and recovery evidence rather than assuming a provider feature guarantees whole-system restoration.

Treat provider settings and harness behavior as version-sensitive: use current primary documentation if details are needed and available; otherwise label them unverified. Do not require an online lookup merely to preserve a code-grounded fact.

For projects using Vercel, Supabase, or Neon, consult the optional [provider checks](providers.md). Record only relevant facts and unknowns; documentation setup does not authorize a security audit or changes to hosted systems.

## Install the project maintenance contract

Adapt the existing instructions rather than replacing them. Link to actual canonical paths. The contract should tell future agents to:

1. Read current state and task-relevant docs, then inspect the repository.
2. Update affected documentation alongside meaningful changes.
3. Record material problems and uncertainty with evidence.
4. Leave checkpoints with actual work location, verification, blockers, and next action.
5. Distinguish tested, deployed, local-only, and pushed state.

Use the bundled AGENTS template as reference, not a wholesale overwrite. Keep the contract useful even if this skill is absent in the next harness. Where multiple contributors work concurrently, place task details in their issue or branch note and keep the project state as an index.

Finish by identifying the engineer and operator reading paths, high-priority gaps, and the limited set of owner questions that would materially improve the docs.
