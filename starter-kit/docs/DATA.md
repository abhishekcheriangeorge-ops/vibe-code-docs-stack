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

[Explain tenant boundaries if applicable, privileged server paths, row-level policies if used, and storage access. For externally reachable data, identify the exposed tables/views/functions or API paths, what enforces authorization, and whether that enforcement was checked. Include bypassing privileged paths and missing or unknown controls; a policy file alone does not prove deployed protection. Link implementation and relevant existing test or security-review evidence. Route sensitive findings using RISKS's audience guidance.]

## Integration contracts

[For actual APIs/webhooks/imports: ownership, auth and webhook verification, payload/schema source, versioning, errors, retry/idempotency semantics, and important examples. Use synthetic examples; do not copy customer data or credentials from fixtures, logs, or production. Do not invent an OpenAPI document for a system that has no corresponding API.]

## Data lifecycle

[Creation/import, correction, export, retention/deletion, synthetic test data, sensitive fields, and audit behavior. Link OPERATIONS for backup and recovery procedures.]
