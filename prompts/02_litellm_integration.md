
Add LiteLLM as the single gateway for ALL LLM calls.

Requirements:
- No direct model calls anywhere else
- Central wrapper (llm_gateway.py)
- Support:
  - Ollama (local)
  - Claude (fallback)

Design for future extensibility.
