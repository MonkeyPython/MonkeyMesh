# Backend

## Structure

```
backend/
├── main.py              # FastAPI app, endpoints
├── router.py            # Model selection logic
├── llm_gateway.py       # LiteLLM wrapper — only LLM entry point
├── config.py            # Settings (pydantic)
├── models/
│   ├── requests.py      # ChatRequest
│   ├── responses.py     # ChatResponse
│   ├── routing.py       # RouterDecision
│   └── gateway.py       # LLMRequest, LLMResponse
├── services/
│   └── chat_service.py  # Orchestrates router + gateway
└── observability/
    └── tracer.py        # Langfuse tracing helpers
```

## Endpoints

| Method | Path | Description |
|---|---|---|
| `GET` | `/` | Serves chat UI |
| `POST` | `/chat` | Main chat endpoint |
| `GET` | `/health` | Health check |

## Rules

- No logic inside endpoints — delegate to service layer
- All LLM calls go through `llm_gateway.call_llm()`
- All model selection goes through `router.route()`
- All types use Pydantic models — no raw dicts

## Adding a new endpoint

1. Define request/response models in `models/`
2. Add business logic in `services/`
3. Wire endpoint in `main.py` — one line delegate

## Configuration

`backend/config.py` — `Settings` model with model strings and feature flags.  
Override at startup via environment variables (pydantic-settings compatible).
