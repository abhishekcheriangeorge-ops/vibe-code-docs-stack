# Engineering guide

Owner: [role/person]. Last setup exercise: [date, environment, code revision, evidence or not exercised].

## Prerequisites and access

[Supported runtime/package manager versions from actual config; required local dependencies; access route for non-production services. Link secure credential locations without values.]

## Clean checkout to running application

| Step | Exact verified command/action | Expected result | Environment |
|---|---|---|---|
| Install | [from real scripts/lockfile] | [observable result] | [local] |
| Configure | [safe .env.example and secret provisioning instructions] | [required variables present] | [local] |
| Prepare data | [migration/seed process] | [synthetic fixtures available] | [disposable/non-production only] |
| Run | [actual command] | [URL and first-success task] | [local] |

Do not leave sample commands that look verified. Mark missing commands as unknown and resolve before engineering handover.

## Validation

| Check | Actual command/procedure | What it establishes | Gaps/dependencies |
|---|---|---|---|
| [Build, test, lint, typecheck, core flow] | [command] | [scope] | [limits] |

## Changing the system

[Repository conventions that are not obvious from the code; safe test-data workflow; migration authoring/application order; regeneration commands for derived types/schema/API references; review/deployment links.]

## Debugging and common setup failures

[Symptom → diagnostic → expected result → next action. Link known gaps to RISKS rather than repeating their full records.]

## Knowledge map

[Entrypoints, domain code, tests, integrations, migrations, configuration. Use links to real files.]
