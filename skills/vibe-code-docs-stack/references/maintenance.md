# Maintenance and checkpoints

## Maintain after a change

Establish the requested change scope from the diff, task, or named files; identify the compared revision or worktree changes rather than assuming HEAD~1 covers the task. Read affected canonical docs and relevant code/tests. Update only the claims and procedures affected by that change; do not regenerate every manual or restructure a working stack.

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

Identify the receiving harness's instruction entry point and whether it loads the canonical maintenance contract, including relevant scoped instructions. Preserve existing rules and add a minimal supported adapter where needed. In the receiving session, check its loaded-instructions view when available and ask it to identify the applicable files and maintenance obligations. If that session is unavailable, mark discovery unverified and leave this check as the next action; do not infer loading from file presence alone.

If returning after an unexpected interruption, reconstruct state from the available code, Git, issues, and evidence. Label uncertainty and continue what is already authorized. Avoid depending on a perfect final session transcript.

For a pause, record why, the return trigger, what still runs or costs money, alert recipient, and responsible owner. Link to relevant provider idle/retention policies, upcoming renewals or expiries, and the latest recovery/export evidence in OPERATIONS. Flag any deadline before the planned return. For retirement, record agreed retention/deletion and access/integration closure work with owners and status. Do not create scheduled jobs, delete infrastructure/data, or revoke access unless authorized.

## Completion evidence

Check changed links and relevant implementation references. Exercise documented commands only when safe, available, and within scope. Record pass/fail/not-run and the reason for important omissions. Report the next action, not a guessed percentage complete.
