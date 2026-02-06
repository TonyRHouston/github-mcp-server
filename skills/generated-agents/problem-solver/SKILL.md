---
name: problem-solver
description: Skill for problem-solver (auto-generated).
keywords: []
source: partially-processed/agents/problem-solver.py
---

name: problem-solver
description: Problem Solver — generates and tries alternative solutions for recurring issues (loops).
keywords: [problem-solver, alternative-solutions]
source: partially-processed/agents/problem_solver.py

# Problem Solver

When to use
- When iterations are stuck in a loop and previous solutions didn't resolve the problem.

Workflow
1. Inspect current iteration and previously tried solutions.
2. Use LLM to generate alternative solutions and record them on the iteration.
3. Try preferred alternatives and update iteration status accordingly.

Dependencies
- `core.agents.troubleshooter.IterationPromptMixin`, `core.llm.parser`.

Output
- Updates `next_state.current_iteration` with `alternative_solutions` and sets iteration status to `PROBLEM_SOLVER` when trying solutions.

## When to use

Use this skill when you need problem-solver automation or guidance.


## Workflow

1. Validate inputs.
2. Run core logic.
3. Return structured output.


## Dependencies

- Repository prompts and templates (check `prompt` paths).
- Access to repo filesystem.


## Output

Structured JSON or markdown describing the result.

