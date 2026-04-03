# Architecture

## Layer overview

```
Request
  └── API (main.py)
        └── Service (chat_service.py)
              ├── Router (router.py)          → selects model
              └── Gateway (llm_gateway.py)    → calls model via litellm
```

## Layers

### API
- FastAPI endpoints
- No logic — delegates immediately to service layer
- Emits trace at boundary

### Service
- Orchestrates router + gateway
- Builds `LLMRequest` from `RouterDecision`
- Manages Langfuse trace lifecycle

### Router
- Accepts `ChatRequest`, returns `RouterDecision`
- Rule-based today; designed for ML swap
- Single entry point: `route(request)`

### Gateway
- Only place LLMs are called
- Accepts `LLMRequest`, returns `LLMResponse`
- Uses litellm — model string determines provider

## Contracts

| Model | Location | Purpose |
|---|---|---|
| `ChatRequest` | `models/requests.py` | API input |
| `ChatResponse` | `models/responses.py` | API output |
| `RouterDecision` | `models/routing.py` | Router output |
| `LLMRequest` | `models/gateway.py` | Gateway input |
| `LLMResponse` | `models/gateway.py` | Gateway output |

## Principles

- LLM is never called outside the gateway
- Router is the single source of truth for model selection
- Every layer is replaceable independently
