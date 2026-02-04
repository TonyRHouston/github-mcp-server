---
name: spec-writer
description: Skill for spec-writer (auto-generated).
keywords: []
source: partially-processed/agents/spec-writer.py
---

name: spec-writer
description: Spec Writer — creates and updates project specifications and initializes projects from user prompts.
keywords: [spec-writer, spec, initialization]
source: partially-processed/agents/spec_writer.py

# Spec Writer

When to use
- When no project specification exists or when updating project specs based on user input.

Workflow
1. Prompt the user for project description (or use `args.initial_prompt`).
2. Use LLM to generate a full specification and a project name.
3. Initialize project state, file system, and epics; set `next_state.specification`.

Dependencies
- `core.templates.registry`, `core.llm.parser.StringParser`, telemetry, UI.

Output
- Sets `next_state.specification`, initializes project metadata and epics; returns special AgentResponse types when needed.

## When to use

Use this skill when you need spec-writer automation or guidance.


## Workflow

1. Validate inputs.
2. Run core logic.
3. Return structured output.


## Dependencies

- Repository prompts and templates (check `prompt` paths).
- Access to repo filesystem.


## Output

Structured JSON or markdown describing the result.

