# Known problems, compromises, and unknowns

Maintainer: [role/person]. Review trigger: [return to active work, incident, milestone, or specified date].

Keep the most consequential unresolved items first. Issue tracker: [canonical location or initial backlog in NOW.md].

Check the intended audience before recording unmitigated vulnerabilities. If this repository is public or its visibility is unknown, keep only a non-exploitable summary, owner, status, and safe reference here. Sensitive reproduction steps, affected identifiers, and incident evidence belong in an approved, access-controlled location outside the public repository. A "private" filename or ordinary public-repository issue provides no protection. If that location is unavailable, record the routing gap; do not publish the details or send an external report without authorization. Never include secret values or customer data.

## R-001 — [Specific concern]

- Category: [known defect / deliberate shortcut / unverified assumption / validation gap / operational gap / security concern].
- Status and owner: [open/accepted/mitigated/resolved; person/role].
- Trigger: [when it occurs or could occur].
- Impact: [user/business consequence, affected scope].
- Evidence and confidence: [audience-appropriate reproduction, test, code/log reference, restricted evidence location, or explicit lack of verification].
- Why accepted, if deliberate: [constraint and ADR link].
- Workaround or containment: [steps/link and limitations; or none].
- Next action: [specific investigation or issue link].
- Revisit trigger: [observable condition or date].
- Last checked: [date and evidence].

Add one record per material concern. Move detailed implementation tasks into audience-appropriate linked issues. Keep resolution evidence discoverable in its appropriate location, and remove obsolete summaries from the active list.

Consider relevant continuity gaps, such as one person's account or recovery device being the only access route, no outage notification, or untested recovery. Record actual findings and unknowns; these prompts do not require a full security audit.
