# Install Vibe Code Docs Stack as an agent skill

For the current task, you can simply give your coding agent the repo link and ask it to follow the skill. Use the [copy-and-paste quickstart](README.md#quick-start-give-this-to-your-coding-agent). Installation is optional and makes the skill discoverable for future tasks in a supported harness.

The self-contained skill is [skills/vibe-code-docs-stack](skills/vibe-code-docs-stack/SKILL.md). Copy the **whole directory**, including references, assets, the bundled [MIT license](skills/vibe-code-docs-stack/LICENSE), and optional UI metadata. The agent needs file access to the target project; the skill itself has no runtime dependency, account connection, or executable hook.

## Codex: ask the built-in installer

In a Codex environment with Skill Installer available, use:

```text
$skill-installer install the skill from
https://github.com/abhishekcheriangeorge-ops/vibe-code-docs-stack/tree/v0.2.0/skills/vibe-code-docs-stack
```

Then select the installed skill and give it a task:

```text
$vibe-code-docs-stack retrofit this project from its code,
existing documentation, and the planning context I provide.
```

Codex CLI and IDE extension support `$` mentions or `/skills`; desktop interfaces may expose a skill picker or `@` selection. Check that the skill appears in your installed skills. Restart the session/app if discovery has not refreshed. [Official OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills)

## Manual installation across harnesses

First clone or download the release into a tools directory outside the target application repository. From that tools directory:

```sh
git clone --depth 1 --branch v0.2.0 https://github.com/abhishekcheriangeorge-ops/vibe-code-docs-stack.git
cd vibe-code-docs-stack
```

Choose **one destination for each harness and scope**. Paths below name the final skill directory, which must contain SKILL.md directly.

| Harness | Personal installation | Project installation |
|---|---|---|
| Codex | `~/.agents/skills/vibe-code-docs-stack/` | `.agents/skills/vibe-code-docs-stack/` |
| Claude Code | `~/.claude/skills/vibe-code-docs-stack/` | `.claude/skills/vibe-code-docs-stack/` |
| Cursor | `~/.cursor/skills/vibe-code-docs-stack/` | `.cursor/skills/vibe-code-docs-stack/` |

Codex documents personal and repository `.agents/skills` discovery. [OpenAI skill locations](https://learn.chatgpt.com/docs/build-skills)

Claude Code documents personal and project `.claude/skills` directories. [Claude Code skills](https://code.claude.com/docs/en/skills)

Cursor supports `.cursor/skills` and `.agents/skills` locations. Its personal cloud-sync behavior differs by location, so prefer `.cursor/skills` for Cursor-specific personal installation and consult its settings for remote use. [Cursor skills](https://cursor.com/docs/skills)

Cursor also discovers Claude and Codex skill directories. If the skill already appears in Cursor, skip an additional Cursor copy unless you need its personal cloud sync.

For example, from this toolkit checkout, install a personal copy for Claude Code with these commands. They refuse an existing destination so an update cannot silently overwrite a customized copy:

```sh
mkdir -p "$HOME/.claude/skills"
if [ -e "$HOME/.claude/skills/vibe-code-docs-stack" ] || [ -L "$HOME/.claude/skills/vibe-code-docs-stack" ]; then
  echo "Skill already exists; review it before updating."
else
  cp -R skills/vibe-code-docs-stack "$HOME/.claude/skills/vibe-code-docs-stack"
fi
```

For a project installation, copy the same directory into the chosen skill parent directory **inside the target application repository**, then commit it with the project. Keep one installed version per harness/scope rather than divergent copies. A supported shared directory can serve multiple tools, but verify each tool's discovery behavior.

The portable core follows the [Agent Skills specification](https://agentskills.io/specification). Harness-specific loading and invocation are not standardized. Tools without native skill support can still read SKILL.md and its bundled resources when explicitly supplied, but will not automatically discover it.

## Invoke it

| Intent | Task text after selecting the skill |
|---|---|
| New project | `Bootstrap the documentation stack from this accepted brief.` |
| Existing project | `Retrofit this project. Preserve useful existing docs and identify missing founder context.` |
| Update after changes | `Maintain the affected docs for this change. Preserve the current structure.` |
| Switch tools or pause | `Create a checkpoint with actual work location, verification, blockers, and next action.` |
| Team handover | `Prepare an operator handover with reading paths, access gaps, and pending exercises.` |
| Read-only review | `Review the documentation gaps and report findings without editing files.` |

In Claude Code, use `/vibe-code-docs-stack` followed by the task. In Cursor, type `/`, find and select the skill, then provide the task. These are natural-language modes, not executable subcommands. [Claude invocation](https://code.claude.com/docs/en/skills), [Cursor invocation](https://cursor.com/docs/skills)

## What persists

The skill contains the method and templates. Each application's documents contain its actual context. During setup, the skill adapts a small maintenance contract in the application's existing agent instructions so future work can follow it even when the skill is absent.

Installing a skill makes it available for selection; it does not schedule background maintenance or guarantee invocation on every coding task. Use the project contract and meaningful checkpoints. Verify that a fresh agent session can find the intent, current state, key risks, and next action.

Local installation also does not transfer credentials, tool connections, or uncommitted project changes to a remote agent. Install the skill in that environment or commit a project-scoped copy, and provision access separately.

## Update an installation

Check [CHANGELOG.md](CHANGELOG.md) for a new tagged release, obtain that release, inspect its skill diff, and replace the installed directory after preserving local customizations. A checkout pinned to a tag does not advance with `git pull`; fetch and select the new tag or download a fresh release. The examples above use a stable tag; `main` is the development branch and can contain changes since the last release.

For copied skills, record the upstream URL and tag or commit in the target's existing tooling/dependency notes. Update deliberate project copies and commit them with the application. Keep project-specific knowledge in project documents, so upgrading the skill does not erase it. For adapted templates, apply useful upstream changes individually rather than replacing completed manuals.

## Maintainer packaging

The root starter-kit directory is the canonical template source. The skill's assets/templates directory is generated from it for standalone distribution. The root LICENSE is canonical and is also bundled into the skill directory. After editing a template or the license, run from the toolkit root:

```sh
python3 scripts/build_skill_assets.py
python3 scripts/build_skill_assets.py --check
```

Commit source changes and their generated copies. Check mode verifies both templates and the bundled license. Edit workflow behavior in SKILL.md and its focused references. The maintainer helper uses Python's standard library; installed agents do not need to execute it.

For a template deletion or rename, review and remove the corresponding obsolete generated file, then rebuild and check. The helper reports unexpected files and does not delete them automatically. The complete validation and release procedure is in [CONTRIBUTING.md](CONTRIBUTING.md).

Research checked: 7 September 2026. Package and behavioral validation are recorded in [SKILL-VALIDATION.md](SKILL-VALIDATION.md); verify discovery in the particular harness/version you use.
