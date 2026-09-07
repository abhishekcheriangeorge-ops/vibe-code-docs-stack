# Fictional examples

These illustrate the level of detail and evidence boundaries. Names, paths, issue numbers, checks, and dates below are fictional; never copy them as facts about a target project. Use only the example relevant to the requested output.

## A short checkpoint

> **Purpose:** Shift Notes helps a small team pass unresolved work to the next shift. Product scope lives in PRODUCT.md.
>
> **Objective:** Let a supervisor correct a submitted note while keeping its original text.
>
> **Actual state:** The local edit path is implemented. The focused edit tests passed in an isolated test database on 7 September; concurrent edits remain untested. No deployment was checked.
>
> **Work location:** Branch `note-corrections`, PR 18. Test evidence is recorded in that PR. The documentation changes in this checkpoint are still local; remote state is unverified.
>
> **Next action:** Inspect the concurrent-edit case in `tests/note_edits.py` and decide the expected conflict behavior with the product owner.
>
> **Decision needed:** Can supervisors correct notes after the next shift has acknowledged them? Owner: product owner. This question also lives in PRODUCT.md; it is not an approved requirement.

This is enough to resume. It does not need padding to reach a word target, and a failed or missing check should remain visible.

## Honest retrospective rationale

> **Decision:** Keep the framework's default database for the prototype.
>
> **Observed implementation:** The current configuration uses that database. The founder confirmed it came from the initial scaffold; no comparison of alternatives was recorded.
>
> **Consequence:** The team's production recovery process is untested. Do not describe the default as a proven scale decision.
>
> **Revisit trigger:** Before onboarding an external team, assign an engineer to verify concurrency and recovery needs against expected usage.

An architecture decision record (ADR) may document a default or uncertainty honestly. It does not need a fabricated selection story.

## A public risk with private evidence

> **Risk:** A security review identified an access-control concern. Technical evidence is restricted to the security owner; remediation tracking is private.
>
> **Owner and next action:** Technical owner to confirm containment and remediation before the next external rollout. Current status: under review. Public documentation will be updated after the disclosure scope is agreed.

The public record gives the team an owner and decision to act on. Reproduction details and sensitive paths belong in the authorized private record, not this summary.
