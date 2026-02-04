---
name: error-handler
description: Skill for error-handler (auto-generated).
keywords: []
source: partially-processed/agents/error-handler.py
---

name: error-handler
description: Error Handler — handles errors returned by other agents, attempts recovery or requests exit.
keywords: [error-handler, recovery, debug]
source: partially-processed/agents/error_handler.py

# Error Handler

When to use
- When another agent returns an error response and recovery or extra diagnostics are required.

Workflow
1. Inspect the `prev_response` (error) and route handling based on agent type (e.g., Executor, SpecWriter).
2. For command errors, prompt user to allow debugging and create a new iteration with diagnostic info.
3. Return `AgentResponse.done` if recovered, or `AgentResponse.exit` to stop orchestrator.

Dependencies
- `core.agents.executor.Executor`, `core.agents.spec_writer.SpecWriter`, LLM prompts for debug analysis.

Output
- May create debugging iterations in `next_state.iterations`, set `next_state.steps`, or signal exit.

## When to use

Use this skill when you need error-handler automation or guidance.


## Workflow

1. Validate inputs.
2. Run core logic.
3. Return structured output.


## Dependencies

- Repository prompts and templates (check `prompt` paths).
- Access to repo filesystem.


## Output

Structured JSON or markdown describing the result.

