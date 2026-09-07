# Maintenance and checkpoints

## Maintain after a change

Establish the requested change scope from the diff, task, or named files. Read affected canonical docs and relevant code/tests. Update only the claims and procedures affected by that change; do not regenerate every manual or restructure a working stack.

| Change | Likely documentation destination |
|---|---|
| Behavior, scope, domain rule | Product and affected user task; acceptance criteria |
| Significant design choice or boundary | Architecture; ADR if consequential |
| Schema, policy, contract, data meaning | Data plus authoritative implementation reference |
| Setup, commands, test process | Engineering |
| Administration, hosted configuration, release, recovery | Operations and relevant runbook |
| New limitation or uncertain assumption | Risks and linked issue |

A brief “not affected” with a reason is valid when no documentation claim changed. Do not add an unrelated Markdown edit just to satisfy a checkbox. Preserve accepted intent when describing an implementation defect; link the discrepancy rather than silently redefining the requirement.

## Checkpoint, pause, or resume

Read the existing current-state document and inspect actual Git state. Capture the facts required to resume: current objective, work branch/location, relevant code revision, active issue/PR, implemented/tested/deployed status, local-only artifacts, blockers, and first next action. Record useful failed approaches only when their evidence will avoid repeated work.

Keep NOW roughly a screen or two, with links for detail. Reference the tested code SHA or CI run; do not claim the document includes its own eventual commit SHA. Mark unverified remote or deployment state explicitly.

Before moving between harnesses or machines, identify which work has actually been committed/pushed and what must still transfer. A checkpoint task alone does not authorize committing, pushing, deploying, or sending external messages. Required secrets and account access are provisioned separately in the receiving environment, not embedded in a handoff.

If returning after an unexpected interruption, reconstruct state from the available code, Git, issues, and evidence. Label uncertainty and continue what is already authorized. Avoid depending on a perfect final session transcript.

For a pause, record why, the return trigger, what still runs or costs money, and the responsible owner. Avoid creating a maintenance schedule or deleting infrastructure unless requested.

## Completion evidence

Check changed links and relevant implementation references. Exercise documented commands only when safe, available, and within scope. Record pass/fail/not-run and the reason for important omissions. Report the next action, not a guessed percentage complete.
