# Skill validation

Package version: 0.1.0. Checked: 7 September 2026.

## Package checks

- The bundled Skill Creator validator passed for SKILL.md metadata and instruction structure.
- Optional OpenAI UI metadata parsed successfully, used the correct skill name, and retained normal implicit discovery.
- Relative links inside the skill resolved within the skill directory; the installed package does not require the parent toolkit checkout.
- The generated asset check matched all 16 bundled templates to the canonical starter-kit files.
- The asset helper was exercised in a temporary fixture: initial generation, clean check, detection of a deliberately stale template without writing in check mode, and regeneration all passed.
- A detached package retained the hidden .github template directory. The ZIP integrity check passed for 22 packaged files.

The package uses plain Markdown, YAML metadata, and template files. The asset helper is a maintainer tool and is not required at skill execution time.

## Independent behavioral exercise

A separate agent used a detached copy of the skill on a small isolated Python CLI fixture. The fixture had existing product/developer documentation, JSON-file persistence, missing historical design rationale, and an explicitly unapproved proposal for cloud hosting.

The task requested a documentation retrofit for resumption and engineer handover, preserving existing useful docs and changing documentation only.

Observed result:

- Preserved existing product and developer guide paths; consolidated architecture/data coverage into the existing guide instead of forcing extra manuals.
- Updated the README and added current state, project instructions, a risk register, and handover preparation.
- Kept the historical cloud proposal unapproved and the JSON-storage rationale unknown.
- Recorded evidence-backed implementation concerns and owner questions.
- Left runtime, deployment, recovery, and recipient acceptance explicitly untested or pending.
- Preserved application source and the historical proposal; accessed no external systems.

The evaluating agent reported 46 local link/anchor checks, implementation-reference checks, syntax parsing, and source-checksum preservation. The resulting current state, developer guide, risk register, and project instructions were inspected afterward.

## Limits

This was one bounded behavioral exercise, not a broad benchmark. It validates useful retrofit behavior on that fixture. It does not establish that every mode behaves correctly on all repositories.

Claude Code and Cursor installation/discovery guidance was reviewed against their primary documentation. No live installation or invocation test was performed in those harnesses. Verify discovery in the actual harness/version before relying on automatic selection. The package does not install hooks, schedule updates, or prove any target application's operational readiness.

See [installation and usage](INSTALL-SKILL.md) for paths and invocation. Repeat a representative isolated exercise when materially changing skill behavior.
