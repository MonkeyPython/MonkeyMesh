# Monkey Mesh

Multi-LLM routing system — local-first, cost-aware, fully observable.

## Stack

- **FastAPI** — API layer
- **LiteLLM** — unified LLM gateway
- **Ollama** — local model inference
- **Langfuse** — tracing and observability

## Quick start

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

See [docs/setup.md](docs/setup.md) for full setup instructions.

## Docs

- [Architecture](docs/architecture.md)
- [Backend](docs/backend.md)
- [Routing](docs/routing.md)
- [Observability](docs/observability.md)
- [Setup](docs/setup.md)
