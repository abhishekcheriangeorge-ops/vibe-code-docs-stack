# Adopting this kit

These files are adaptable templates, not documentation of an audited application.

Read the [documentation playbook](../documentation-playbook.md) and [START-PROJECT prompt](../START-PROJECT.md). Copy only the files appropriate to your project's stage and merge with existing docs and agent instructions. Replace bracketed placeholders with verified facts, explicit unknowns, or a justified “not applicable.” Delete template guidance after adaptation.

Begin with README, NOW, AGENTS, PRODUCT, ARCHITECTURE, and RISKS. Add ENGINEERING when runnable, DATA when persistent, OPERATIONS when hosted, and USER-GUIDE before others use the product. This kit includes later-stage files so you have their templates ready; their presence does not make your project ready for handover.

The decision, runbook, and handover files under templates/ are sources for documents you create when needed. The portfolio template belongs once in your private project index, rather than in every application repo.

CLAUDE.md imports the common contract for Claude Code. Keep any necessary harness-specific additions small. Verify that your actual tools load the intended instructions. A Markdown instruction is guidance, not an enforcement mechanism.

No application commands, credentials, infrastructure, CI workflow, or account integrations have been configured by this kit. Adapt the PR template to the repository's actual workflow.
