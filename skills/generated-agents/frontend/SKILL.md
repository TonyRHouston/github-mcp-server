---
name: frontend
description: Skill for frontend (auto-generated).
keywords: []
source: partially-processed/agents/frontend.py
---

name: frontend
description: Frontend — builds and iterates on the frontend, processes template outputs and auto-debug flows.
keywords: [frontend, build, ui]
source: partially-processed/agents/frontend.py

# Frontend

When to use
- To generate or continue building the frontend part of the project, including template application and UI iteration.

Workflow
1. Start frontend flow: clear logs, announce build, and call LLM template `build_frontend`.
2. Process returned code blocks, apply changes, optionally run auto-debug and iteration logic.
3. When finished, set frontend iteration flags and possibly move to backend steps.

Dependencies
- `core.llm.parser.DescriptiveCodeBlockParser`, `core.agents.git.GitMixin`, process manager for auto-debug.

Output
- Writes frontend files, updates `next_state.epics` messages and `fe_iteration_done` flags, and may update knowledge base.

## When to use

Use this skill when you need frontend automation or guidance.


## Workflow

1. Validate inputs.
2. Run core logic.
3. Return structured output.


## Dependencies

- Repository prompts and templates (check `prompt` paths).
- Access to repo filesystem.


## Output

Structured JSON or markdown describing the result.

