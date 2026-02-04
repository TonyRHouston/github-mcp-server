---
name: importer
description: Skill for importer (auto-generated).
keywords: []
source: partially-processed/agents/importer.py
---

name: importer
description: Importer — inspects and imports existing projects into the workspace and summarizes them.
keywords: [importer, project, analyze]
source: partially-processed/agents/importer.py

# Importer

When to use
- When onboarding an existing project into the MCP workspace for analysis or conversion.

Workflow
1. Ask user to copy project files to the project root and confirm.
2. Call `state_manager.import_files()` and analyze entry points via an LLM prompt.
3. Populate `Specification` and initial epics based on detected project structure.

Dependencies
- `core.db.models.Complexity`, `core.templates.example_project.EXAMPLE_PROJECT_DESCRIPTION`, telemetry.

Output
- Updates `next_state.specification`, `next_state.epics`, and may emit `AgentResponse.describe_files`.

## When to use

Use this skill when you need importer automation or guidance.


## Workflow

1. Validate inputs.
2. Run core logic.
3. Return structured output.


## Dependencies

- Repository prompts and templates (check `prompt` paths).
- Access to repo filesystem.


## Output

Structured JSON or markdown describing the result.

