---
name: architect
description: Skill for architect (auto-generated).
keywords: []
source: partially-processed/agents/architect.py
---

name: architect
description: Architect — plans project architecture, selects templates, and records system/package dependencies.
keywords: [architect, templates, architecture]
source: partially-processed/agents/architect.py

# Architect

When to use
- When starting a new project or selecting starter templates; when defining system and package dependencies.

Workflow
1. Read current `Specification` from state.
2. Use LLM prompts (`select_templates`, `technologies`) to propose architecture and templates.
3. Validate compatibility and populate `spec.system_dependencies` and `spec.package_dependencies`.
4. Update `next_state.specification` and set `next_state.action` to the architecture step.

Dependencies
- `core.templates.registry`, `core.llm.parser`, `core.db.models.Specification`, telemetry utilities.

Output
- Updates `next_state.specification`, `next_state.action`, and telemetry tags; may create project template instances.

## When to use

Use this skill when you need architect automation or guidance.


## Workflow

1. Validate inputs.
2. Run core logic.
3. Return structured output.


## Dependencies

- Repository prompts and templates (check `prompt` paths).
- Access to repo filesystem.


## Output

Structured JSON or markdown describing the result.

