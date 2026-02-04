Generated agent SKILLs
======================

These `SKILL.md` files were generated from Python agent implementations under `partially-processed/agents/`.

Purpose
- Provide a minimal, standardized skill frontmatter and sections so skills can be discovered and reviewed.

What these SKILLs need to operate standalone
- Prompts/templates directory referenced by the agent (check `core/llm` and repo `prompt` paths).
- Any tool adapters or allowed-tools declarations needed by the skill (e.g., `Bash`, `Git`).
- Optional: example `inputs` and sample `expected_output` to make testing easier.

Next steps
- Review each SKILL.md and refine `description`, `keywords`, and `Dependencies` to list exact prompt paths and tool permissions.
- Add `allowed-tools` frontmatter if a skill needs to call shell or external tools.
