# Vibe Code Docs Stack

**Remember why you built it. Know where you left it. Hand it over with confidence.**

A practical documentation system for people building software with AI coding tools. Preserve product intent, design decisions, known problems, and operating instructions in the repository so the context travels with the code.

Built for solo builders, frequent project switchers, and teams taking prototypes into long-term ownership. Start small and add documentation as the project earns it.

## Start here

| Your situation | What to use |
|---|---|
| I want to install this as an agent skill | [Skill installation and usage](INSTALL-SKILL.md) |
| I already have a project | [Retrofit an existing project](prompts/RETROFIT-PROJECT.md) |
| I'm starting a new project | [Set up the documentation stack](START-PROJECT.md) |
| I want the reasoning and full workflow | [Research and playbook](documentation-playbook.md) |
| I want the actual document templates | [Starter kit](starter-kit/ADOPTING-THIS-KIT.md) |
| I'm transferring responsibility | [Handover evidence template](starter-kit/templates/HANDOVER.md) |

## Use it as an agent skill

Install the self-contained [Vibe Code Docs Stack skill](skills/vibe-code-docs-stack/SKILL.md) once in your harness or commit it into a target project's skill directory. Then select it and ask it to bootstrap, retrofit, maintain, checkpoint, or prepare a handover.

```text
Use vibe-code-docs-stack to retrofit this project's documentation.
Preserve existing useful docs and identify missing product context.
```

The skill bundles its references and templates, with optional Codex UI metadata and no runtime dependency. [Installation instructions](INSTALL-SKILL.md) cover Codex, Claude Code, and Cursor. The prompts below remain available for tools without skill support.

## Use it on an existing project

1. Open the target project in your coding agent with repository access.
2. Paste the [retrofit prompt](prompts/RETROFIT-PROJECT.md).
3. Provide relevant proposals, planning notes, or conversation extracts. Ask the agent to distinguish historical intent from current implementation.
4. Review the questions about purpose and design reasoning that only you can answer.
5. Review and commit the resulting documentation alongside the code.
6. Start a fresh agent session. Ask it to explain the system, find the main risks, and identify the next action using the repository alone.

The prompt is sufficient to begin. Use the starter-kit files when you want the exact templates; merge them into the target project's existing documentation rather than overwriting useful material.

## Use it on a new project

Paste the main prompt from [START-PROJECT.md](START-PROJECT.md) into your coding agent alongside the project brief. Have it fill a short initial stack from accepted decisions, then maintain affected documents as implementation progresses.

When turning a long planning conversation into a brief, separate **accepted decisions**, **proposals**, **assumptions**, and **unresolved questions**. The setup file also includes prompts for ending a planning conversation, resuming work, and making a checkpoint.

## The stack

| Document | Purpose | Create when |
|---|---|---|
| [README.md](starter-kit/README.md) | Entry point and audience reading paths | Project inception |
| [NOW.md](starter-kit/NOW.md) | Current objective, actual state, work location, next action | Project inception |
| [AGENTS.md](starter-kit/AGENTS.md) | Shared project instructions for coding agents | Project inception |
| [PRODUCT.md](starter-kit/docs/PRODUCT.md) | Problem, users, scope, business rules, intent | Project inception |
| [ARCHITECTURE.md](starter-kit/docs/ARCHITECTURE.md) | Current design, dependencies, tradeoffs, evidence | Initial design |
| [RISKS.md](starter-kit/docs/RISKS.md) | Defects, deliberate shortcuts, assumptions, validation gaps | Initial design |
| [ENGINEERING.md](starter-kit/docs/ENGINEERING.md) | Setup, real commands, tests, development workflow | Once runnable |
| [DATA.md](starter-kit/docs/DATA.md) | Schema sources, meaning, ownership, access, lifecycle | Once data persists |
| [OPERATIONS.md](starter-kit/docs/OPERATIONS.md) | Administration, environments, releases, diagnosis, recovery | Once hosted or administered |
| [USER-GUIDE.md](starter-kit/docs/USER-GUIDE.md) | First success, routine user tasks, common errors | Before others use it |

Begin with six short documents. Add the others when their responsibilities appear. For an existing hosted application, most of these triggers may already apply. Existing equivalent documents can keep their names and locations.

Additional templates cover [design decisions](starter-kit/templates/DECISION.md), [runbooks](starter-kit/templates/RUNBOOK.md), [handover exercises](starter-kit/templates/HANDOVER.md), a private [portfolio index](starter-kit/templates/PORTFOLIO.md), and a [PR documentation-impact question](starter-kit/.github/pull_request_template.md).

## Preserve the reasoning

The next engineer needs to understand the constraint a choice solved, the compromise it introduced, and when to reconsider it.

For consequential decisions, record:

- Context and constraints at the time.
- The decision and alternatives actually considered.
- Rationale, consequences, and related risks.
- A concrete revisit trigger.
- Evidence, owner, and status.

Code can establish what was implemented. Historical intent needs a source or confirmation. Label inferred reasoning explicitly.

## Keep it current

At the start of work, read the project instructions and current state. With meaningful changes, update the affected canonical documents. At useful checkpoints, update NOW.md with actual validation, deployment state, local-only work, blockers, and the first next action.

Give each fact one home. Link implementation work to the canonical issue tracker. Keep human and agent handovers as reading paths through the same documents, with a dated record of responsibilities and practical exercises.

Instructions guide the agent; checks and practical handover exercises establish what works. The included templates do not configure CI, integrations, accounts, deployments, or recovery.

## Moving between coding tools

The kit uses a shared AGENTS.md contract and a small [CLAUDE.md adapter](starter-kit/CLAUDE.md) that imports it. Verify the receiving tool loads the intended instructions, and transfer the relevant code and documents together. Required context should not live only in a local chat or an agent's private memory.

Tool-specific behavior and references are documented in the [playbook](documentation-playbook.md). Recheck provider guidance when adopting the kit, as tools and hosted services change.

## Research foundations

The playbook draws on Docs as Code, Diátaxis, arc42, architecture decision records, the C4 model, Google SRE guidance, and official documentation for coding tools, Vercel, Supabase, and Neon. Sources are linked beside their supporting claims in the [playbook](documentation-playbook.md).

The file layout and lifecycle recommendations are a practical synthesis. The templates are starting points to fill with project-specific evidence.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Improvements should make documentation easier to use, verify, and maintain without creating duplicate sources of truth.
