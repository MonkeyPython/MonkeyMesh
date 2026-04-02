# CLAUDE SYSTEM (V9)

## Goal
Correct results with minimal tokens.

## Modes

### direct (default)
- single-step
- no agents

### agent
- use one agent
- structured tasks only

## Rules
- Keep context minimal
- Prefer direct execution
- Use agent only for structured tasks
- Plan briefly before complex tasks

## Model Policy
- haiku: large/simple tasks
- sonnet: default (code, structured)
- opus: only if necessary

## Validation
- Must follow schema
- Must respect constraints

## Output
- Only result
- No verbosity
