# Handover evidence — [project, recipient, date]

Scope: [product use / daily administration / engineering / production operation / combination].

Outgoing owner: [person]. Incoming owner: [person]. Reviewed code/release/environment: [reference].

This is a dated acceptance record linking the current manuals. Do not copy the manuals into it.

## Reading path

[Link README, NOW, PRODUCT, ARCHITECTURE, RISKS, and role-relevant manuals.]

## Responsibility transfer

| Responsibility | Incoming owner | Access and ownership evidence | Effective date | Remaining owner/gap |
|---|---|---|---|---|
| [Responsibility] | [person/role] | [evidence or no] | [date] | [gap] |

For account responsibilities, distinguish usable access from owner-level control and billing/renewal transfer. Link the restricted access review in OPERATIONS: human and machine access, MFA/recovery custody, necessary credential rotation/revocation and verification, and remaining gaps. Record outgoing access as revoked on a date or deliberately retained with scope, accountable owner, and end/review date. Responsibility transfer does not by itself require the founder to lose access or authorize account changes.

## Practical exercises

Select exercises appropriate to the responsibility being transferred and the recipient's existing authorization. Mark not applicable with a reason rather than treating every role as a production engineer. Record an unrun exercise as a gap; documentation delivery does not authorize operational changes.

| Exercise | Recipient result and evidence | Gap, owner, next action |
|---|---|---|
| Explain purpose, scope, design tradeoffs, and key limitations | [result] | [gap] |
| User: reach the first useful outcome from USER-GUIDE and recover from a common input error | [result] | [gap] |
| Engineer: clean checkout, run, trace a core flow; explain migration/recovery constraints | [result] | [gap] |
| Engineer: small change, relevant checks, preview deployment if authorized | [result] | [gap] |
| Technical operator: diagnose a representative failure; receive a test alert if configured | [result] | [gap] |
| Recovery owner: recover into a named disposable target with outgoing side effects disabled or routed to test integrations; verify and clean up | [source/destination and result; OPERATIONS procedure] | [gap] |
| Administrator: complete routine user/record management tasks | [result] | [gap] |
| Administrator: handle common failure and escalate | [result] | [gap] |
| Owner: verify account ownership, access review, billing, renewals, monitoring ownership | [result] | [gap] |

## Accepted scope and open responsibilities

[Explicitly state what the recipient can now own and what remains with someone else. Record critical gaps and their resolution plan. Do not infer acceptance merely from delivering files.]
