# Administration and service operations

Owner: [role/person]. Last reviewed against live configuration: [date, environment, evidence or not verified].

## Start here

- Service/dashboard: [verified link].
- Routine administration: [section or runbook links].
- Something is broken: [diagnostic entry point and responsible role].
- Escalation: [who, how, what evidence to provide without exposing sensitive data].
- Support expectation: [hours and response commitment, or best effort/no commitment; provider support route where relevant].

## Ownership, access, and obligations

| Service/account and plan | Purpose | Owner and access route | Billing/renewal responsibility | Failure consequence |
|---|---|---|---|---|
| [Code host/app host/database/domain/email/etc. actually used; plan checked on date] | [purpose] | [person/role + secure location] | [owner; cost verified on date] | [effect] |

Keep internal account and access details in an approved, access-controlled companion record outside a public repository. Never include passwords, tokens, recovery codes, or full credential-bearing database URLs. Link that record and its owner without disclosing sensitive details.

For relevant services, record:

- Access continuity: personal or organization ownership, owner-level role, second owner or emergency route, MFA/recovery custody location, and any single-owner gap.
- Access review: human and machine access (tokens, apps, deploy hooks, integrations), owner and scope, last review date, and revoke/rotate or deliberate retention decisions. Link credential procedures by name, consumers, replacement order, and verification; keep values in the secure source.
- Plan constraints: actual backup coverage, inactivity/expiry behavior, usage restrictions, and date checked. Use "none" or "not verified" where appropriate.
- Cost controls: main usage drivers, configured limit or alert, recipient, and what happens at the limit (service stops, overage billed, or unknown).

## Environment map

| Environment | App URL / hosting project | Database project/branch | Auth/storage/integrations | Configuration source |
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

[State how an outage is noticed: configured monitoring and recipients, or none/unknown. Record log locations, access and retention, last test-alert result where relevant, and the incident-record location. Keep security incident details access controlled; identify the responsible owner and containment/escalation runbook for suspected credential or data exposure where applicable.]

| Symptom/alert | User impact | Where to look | First safe diagnostic | Escalation/runbook |
|---|---|---|---|---|
| [Observed/anticipated relevant failure] | [effect] | [dashboard/log link] | [step] | [role/link] |

## Recovery

- Application rollback: [procedure, eligibility, configuration caveats, database compatibility, verification].
- Database recovery: [actual backup/restore coverage or none, retention, source and destination identifiers, procedure, verification].
- Uploaded files/object storage recovery: [separate coverage and procedure, or not applicable].
- Configuration and external state: [secure settings/credential recovery source and date; DNS, auth, payments, or other state requiring separate recovery/reconciliation; known gaps].
- Acceptable data loss: [desired interval and owner agreement].
- Desired recovery time: [target, distinguished from demonstrated result].
- Last isolated recovery exercise: [date, result, evidence, gaps; or never exercised].

Before an exercise, identify the exact backup/source and a separate disposable destination project, database, or branch with appropriate data access controls. Check which target the restore operation writes to; an in-place restore can overwrite that target. Never use production as the exercise destination. Disable outgoing side effects or route jobs, email, payments, webhooks, and other integrations to test modes before running the restored system. Record verification and cleanup steps, within the owner's role and existing authorization.

## Routine maintenance and leaving the project paused

[Owner and trigger for dependency updates, failed jobs, backup verification, cost review, branch cleanup, domain/billing renewals. State what remains active during a pause, who receives alerts, and expected resume steps. Note provider inactivity behavior and the next relevant expiry, restore-window, runtime-support, or renewal deadline; record a review date before it. Link current recovery evidence rather than assuming backups exist.]

## Responsibility boundaries

[Which tasks operators may perform; which require an engineer; current production owner; unresolved handover responsibilities with owners and links.]
