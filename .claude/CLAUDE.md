
# Monkey Mesh

Multi-LLM routing system.

## Rules
- Use router for model selection
- Use llm_gateway for all LLM calls
- Always trace with Langfuse
- Keep code simple and typed
- Create a new git branch before coding
- Make atomic commits per topic
- NEVER include co-authored-by in commits

## Architecture
API → Router → Gateway → Models
