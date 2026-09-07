# Administration and service operations

Owner: [role/person]. Last reviewed against live configuration: [date, environment, evidence or not verified].

## Start here

- Service/dashboard: [verified link].
- Routine administration: [section or runbook links].
- Something is broken: [diagnostic entry point and responsible role].
- Escalation: [who, how, what evidence to provide without exposing sensitive data].

## Ownership, access, and obligations

| Service/account | Purpose | Owner and access route | Billing/renewal responsibility | Failure consequence |
|---|---|---|---|---|
| [GitHub/Vercel/database/domain/email/etc. actually used] | [purpose] | [person/role + secure location] | [owner; cost verified on date] | [effect] |

Keep internal account details in a private companion record when this repository is public. Never include passwords, tokens, recovery codes, or full credential-bearing database URLs.

## Environment map

| Environment | App URL / Vercel project | Database project/branch | Auth/storage/integrations | Configuration source |
|---|---|---|---|---|
| Local | [target] | [target] | [targets] | [location, no secret values] |
| Preview | [target] | [target; data-copy policy] | [targets] | [scope/overrides] |
| Production | [target] | [target] | [targets] | [scope] |

Add staging only if it exists. Verify that previews target the intended backend and integration modes.

## Configuration reference

| Variable/setting name | Purpose | Server/client exposure | Environment/scope | Secure source / owner |
|---|---|---|---|---|
| [Name only] | [purpose] | [exposure] | [scope] | [location/role] |

[Record dashboard-only settings, domains/DNS, auth redirect configuration, schedules, webhooks, and feature flags actually used. Link .env.example where it exists.]

## Product administration

[Document only supported tasks: onboarding/offboarding, roles, corrections, approvals, imports/exports, reconciliation, retries, and support. For each give required role, steps, expected result, verification, and escalation. Link long procedures. Identify missing admin capabilities and manual workarounds.]

## Releases

[Who owns deployment; actual trigger; required checks; migration/application order; compatibility; smoke checks; how to identify deployed commit; link to the canonical release record.]

## Diagnosis and alerts

| Symptom/alert | User impact | Where to look | First safe diagnostic | Escalation/runbook |
|---|---|---|---|---|
| [Observed/anticipated relevant failure] | [effect] | [dashboard/log link] | [step] | [role/link] |

## Recovery

- Application rollback: [procedure, eligibility, configuration caveats, database compatibility, verification].
- Database recovery: [actual backup/restore coverage, retention, target, procedure, verification].
- Uploaded files/object storage recovery: [separate coverage and procedure, or not applicable].
- Acceptable data loss: [desired interval and owner agreement].
- Desired recovery time: [target, distinguished from demonstrated result].
- Last isolated recovery exercise: [date, result, evidence, gaps; or never exercised].

## Routine maintenance and leaving the project paused

[Owner and trigger for dependency updates, failed jobs, backup verification, cost review, branch cleanup, domain/billing renewals. State what remains active during a pause and who receives alerts.]

## Responsibility boundaries

[Which tasks operators may perform; which require an engineer; current production owner; unresolved handover responsibilities with owners and links.]
