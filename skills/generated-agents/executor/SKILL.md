---
name: executor
description: Skill for executor (auto-generated).
keywords: []
source: partially-processed/agents/executor.py
---

name: executor
description: Executor — runs shell commands, streams output to the UI, and analyzes results with the LLM.
keywords: [executor, run, cli]
source: partially-processed/agents/executor.py

# Executor

When to use
- When a task step includes a `command` to run locally as part of implementation or debugging.

Workflow
1. Confirm command with user (ask_question), optionally edit.
2. Run command via `ProcessManager.run_command`, stream stdout/stderr to UI.
3. Evaluate command output with an LLM (`ran_command` prompt) and return `CommandResult` analysis.
4. Log execution and record `ExecLog` via state manager.

Dependencies
- `core.proc.process_manager.ProcessManager`, `core.llm.parser.JSONParser`, `core.proc.exec_log.ExecLog`.

Output
- Persists `ExecLog` entries, sets `next_state.action` and may return AgentResponse.done or AgentResponse.error with details.

## When to use

Use this skill when you need executor automation or guidance.


## Workflow

1. Validate inputs.
2. Run core logic.
3. Return structured output.


## Dependencies

- Repository prompts and templates (check `prompt` paths).
- Access to repo filesystem.


## Output

Structured JSON or markdown describing the result.

