# Architecture and rationale

Owner: [role/person]. Implementation inspected: [code revision and date].

## Current system

[Explain what runs where, who uses it, and external services. Add a concise context/container diagram based on observed configuration. Label proposed elements explicitly.]

## Main workflow

[Trace one important action through interface, authentication/authorization, processing, database, and external side effects. Include a failure/retry path. Add a sequence diagram only if it clarifies ordering.]

## Component map

| Responsibility | Actual code/config location | Data or external dependency | Failure consequence |
|---|---|---|---|
| [Component] | [path] | [dependency] | [effect] |

## Why this design

[Constraints and concise rationale. Link major choices to decisions/. Mark historical rationale inferred from code as unconfirmed.]

| Decision | Current status | Record | Revisit trigger |
|---|---|---|---|
| [Choice] | [accepted/proposed/superseded] | [ADR link] | [condition] |

## Boundaries and cross-cutting behavior

[Identity, permissions, tenant isolation if applicable, server/client boundary, errors, logging, retries/idempotency, concurrency, third-party contracts. Include only relevant concerns and link to DATA/OPERATIONS details.]

## Evidence and limits

| Concern | Measured fact | Assumption or unknown | Investigation/revisit trigger |
|---|---|---|---|
| [Load, latency, file size, concurrency, recovery] | [result + evidence or not measured] | [uncertainty] | [condition] |

## Where an incoming engineer should look

[Link priority RISKS entries and the parts of the system most likely to require assessment. Distinguish intentional prototypes from known defects.]
