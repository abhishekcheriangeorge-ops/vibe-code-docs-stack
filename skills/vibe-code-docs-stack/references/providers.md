# Provider details that change documentation decisions

Read only the sections matching the target stack. Supporting provider pages were re-read on 7 September 2026; this verifies the claims below, not any target project's configuration. Recheck relevant pages when adopting this guidance or when the plan, integration, or recovery method changes. Record actual settings and evidence in the project's existing engineering, data, and operations documents.

Documentation work does not authorize creating branches, copying data, running migrations, deploying, restoring, or changing access. A recovery exercise needs a named disposable target, a method that leaves production untouched, appropriate access to copied data, and test configuration that prevents real emails, payments, webhooks, and jobs. Record verification and cleanup responsibility; do not execute a provider's production Restore action as a rehearsal.

## Supabase

For Data API access, establish exposed schemas, table grants, row-level security (RLS) enablement, policies by role, and evidence for permitted and denied access. Also identify exposed views/functions and privileged server paths: secret and legacy `service_role` keys bypass RLS, so those paths need their own authorization. Record key types and variable names, never values. The provider currently recommends publishable/secret keys and describes the legacy keys' deprecation; establish the project's migration status without assuming a variable name proves its type. [RLS](https://supabase.com/docs/guides/database/postgres/row-level-security), [API keys](https://supabase.com/docs/guides/getting-started/api-keys)

Record relevant Security Advisor findings or that they were not inspected. Review account MFA and recovery ownership when assessing production readiness. An advisor result does not establish that the application's access rules are correct. [Production checklist](https://supabase.com/docs/guides/deployment/going-into-prod)

Supabase Branching provides separate instances and credentials. New branches start without production data or Storage objects by default; seeds or the dashboard's Include data option change that. Establish which branch/project each preview actually uses, copied data, configuration, connected services, and cleanup. [Branching](https://supabase.com/docs/guides/deployment/branching)

Database backups exclude Storage objects. Automatic daily backups are a paid-plan feature; the backup guide recommends off-site exports for Free projects. Record available backups, retention, and independent file recovery. In-project restoration takes the project offline. For a rehearsal, use an eligible **Restore to a new project**, or a logical backup restored into a separate disposable project following the provider guide. The new-project feature is a database copy: Storage objects/settings, Edge Functions, Auth settings/API keys, and other listed configuration need separate handling. [Backups](https://supabase.com/docs/guides/platform/backups), [new-project restore](https://supabase.com/docs/guides/platform/clone-project), [logical restore](https://supabase.com/docs/guides/platform/migrating-within-supabase/backup-restore)

Record which connection mode each application, migration, and backup tool uses. Supavisor transaction mode does not support prepared statements; direct connections have network requirements that differ from session pooling. Check the provider and the actual driver/tool versions. [Connection methods](https://supabase.com/docs/guides/database/connecting-to-postgres)

## Neon

Ordinary branches inherit parent data; independent writes do not make that data non-sensitive. Record parent, copy/seed/schema-only policy, access, and expiry or cleanup. A Git merge needs an explicit database migration workflow. [Branching](https://neon.com/docs/introduction/branching), [branch creation](https://neon.com/docs/manage/branches)

For an isolated recovery copy, create a **new branch from past data**, within available source history, and use its own endpoint. **Instant restore** instead replaces the selected target's database timeline, affects every database on that branch, and interrupts connections. Current instant restore requires root-branch history; it also restores database-held Auth state but does not revert Object Storage or Functions. Record what the exercise actually recovers. [Branch creation](https://neon.com/docs/manage/branches), [instant restore](https://neon.com/docs/postgres/backup-restore/branch-restore)

Record the configured history window and earliest usable recovery point, including plan limits; a Free plan is not equivalent to having no recovery, and a history window is not a lasting off-site backup. [History window](https://neon.com/docs/postgres/backup-restore/history-window)

Record whether Vercel preview branching is enabled and which integration manages it. In the Vercel-managed integration, branch variables are injected at deployment time and cannot be viewed in project environment-variable settings. Use existing redacted deployment/integration evidence to establish the target without revealing connection strings. Cleanup follows deployment removal, which may occur much later than PR closure; record the actual retention policy. [Vercel-managed integration](https://neon.com/docs/guides/vercel-managed-integration)

Document pooled/direct connection names and tool compatibility. Neon supports protocol-level prepared statements through its pooler; SQL-level prepared statements and session-dependent operations have limits. Direct connections are the documented choice for `pg_dump` and tools needing persistent sessions. Do not apply Supavisor's prepared-statement rule to Neon. [Connection pooling](https://neon.com/docs/connect/connection-pooling)

## Vercel

Map development, preview, production, and any custom environments, including branch overrides and integration-managed variables. Record names, client/server exposure, type, and secure source; Secret values are write-only after saving. Changes apply to new deployments. Verify who can reach each preview and the actual protection scope; frontend protection and backend authorization address different access paths. [Environment variables](https://vercel.com/docs/environment-variables), [Deployment Protection](https://vercel.com/docs/deployment-protection)

Git integration deploys branch pushes by default. A migration in the build command therefore runs for builds that reach that step, against the database resolved there. Record migration runner, target, ordering, and guards per environment; a preview build must not incidentally migrate production. [Git deployments](https://vercel.com/docs/git/vercel-for-github)

Instant Rollback reuses the prior deployment's configuration and cron definitions and disables automatic production-domain assignment. Record eligible targets, database compatibility, and how the operator promotes the fix and verifies normal promotion resumes. It does not rewind an external database. [Instant Rollback](https://vercel.com/docs/instant-rollback)

## Plans, evidence, and long pauses

For each service, record plan/add-ons, usage drivers, limits, action at the limit, alert recipient, log retention, and idle/expiry behavior with a source and date. Preserve sanitized diagnostic evidence at appropriate visibility before logs expire. Vercel's spend threshold only pauses production when that action is enabled; Supabase's Spend Cap covers selected usage items, not the whole bill. [Runtime logs](https://vercel.com/docs/logs/runtime), [Vercel Spend Management](https://vercel.com/docs/spend-management), [Supabase cost control](https://supabase.com/docs/guides/platform/cost-control)

Before a long pause, establish a usable database/file recovery source, provider resume deadlines, runtime and credential expiry, and the next review before the earliest relevant deadline. Supabase distinguishes resuming a paused project from downloading its backup after the platform restore window; do not describe this as automatic data deletion. Also check whether the current plan permits the intended use. [Supabase pause recovery](https://supabase.com/docs/guides/platform/upgrading#time-limits), [Supabase plan features](https://supabase.com/pricing), [Vercel Hobby](https://vercel.com/docs/plans/hobby)
