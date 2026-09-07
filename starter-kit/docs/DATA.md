# Data and contracts

Owner: [role/person]. Schema inspected: [source revision, target environment, date].

## Authority and applied state

- Schema/migration source: [actual paths and tooling].
- How applied migration state is checked: [verified process].
- Last comparison and drift: [result or unknown].
- Generated types/reference: [source, generator/version/command, output paths or not used].

## Model and meaning

[Add an entity relationship diagram matching the actual schema. Explain concepts and relationships; avoid manually duplicating every generated column declaration.]

| Entity or important field | Business meaning | Ownership/source | Constraints and lifecycle |
|---|---|---|---|
| [Name] | [meaning, units/timezone if applicable] | [owner/source] | [nullability meaning, deletion, retention, state transitions] |

## Access model

| Actor/role | Read/write scope | Enforcement location | Verification |
|---|---|---|---|
| [Role] | [scope] | [policy/code path] | [test evidence or not verified] |

[Explain tenant boundaries if applicable, privileged server paths, row-level policies if used, and storage access. Link implementation.]

## Integration contracts

[For actual APIs/webhooks/imports: ownership, auth, payload/schema source, versioning, errors, retry/idempotency semantics, and important examples. Do not invent an OpenAPI document for a system that has no corresponding API.]

## Data lifecycle

[Creation/import, correction, export, retention/deletion, synthetic test data, sensitive fields, and audit behavior. Link OPERATIONS for backup and recovery procedures.]
