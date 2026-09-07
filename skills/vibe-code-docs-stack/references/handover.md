# Handover by responsibility

Establish what the recipient will own: engineering, product administration, technical operations, or a combination. If unknown, prepare the reading paths and list the scope question without granting ownership or access.

Use the document map and relevant canonical manuals. Create a dated handover record from the bundled template, linking these documents. Avoid another independent copy of the system description. Record outgoing/incoming owner, reviewed release or code revision, environment, access status, and remaining responsibilities.

## Select practical exercises

For an engineer: explain product purpose and major tradeoffs, run from a clean checkout, trace a core flow, identify priority risks, and make and verify a small change. Preview deployment and isolated recovery exercises belong only within the recipient's assigned role and actual authorization.

For a product administrator: complete real routine tasks such as user/role management, approvals, corrections, or imports; identify expected outcomes; handle a representative error; and demonstrate escalation. Do not imply admin capabilities exist when they are manual workarounds or missing features.

For a technical operator: identify the live environment and release, locate monitoring/logs, diagnose a representative failure, explain release and migration compatibility, and exercise recovery in an isolated environment before taking recovery responsibility. Verify account, billing, renewal, and maintenance ownership.

If the user asked to prepare the handover, document the exercises as pending. Do not execute deployments, grant access, or simulate a recipient's acceptance to make the record look complete. Run authorized local exercises when requested; describe exactly what they establish.

## Assess readiness

For each responsibility, record evidence, gaps, owner, and next action. Use scoped conclusions such as “ready for daily administration; recovery remains with the current technical owner.” Document delivery or an agent reading the manual does not establish the recipient can operate the system.

Preserve any meaningful lessons from the exercises in the canonical manuals, so the next handover benefits without another parallel documentation set.
