---
name: orchestrator
description: Skill for orchestrator (auto-generated).
keywords: []
source: partially-processed/agents/orchestrator.py
---

name: orchestrator
description: Orchestrator — main control loop that selects, runs, and coordinates agents based on project state.
keywords: [orchestrator, control, loop]
source: partially-processed/agents/orchestrator.py

# Orchestrator

When to use
- Always runs as the top-level controller to decide which agent should run next and manage commit points.

Workflow
1. Initialize UI, dependencies, and ProcessManager/Executor.
2. In a loop: update stats, create appropriate agent(s) for current step, run them (serial or parallel), and handle responses.
3. Manage git initialization, template application, and final exit conditions.

Dependencies
- Imports many agents (`Architect`, `BugHunter`, `Developer`, etc.), `core.ui`, `ProcessManager`, and state manager.

Output
- Drives `next_state` commits, selects agents, and orchestrates task lifecycle; returns True on successful exit.

## When to use

Use this skill when you need orchestrator automation or guidance.


## Workflow

1. Validate inputs.
2. Run core logic.
3. Return structured output.


## Dependencies

- Repository prompts and templates (check `prompt` paths).
- Access to repo filesystem.


## Output

Structured JSON or markdown describing the result.

