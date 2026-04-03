# Monkey Mesh

Multi-LLM routing system — local-first, cost-aware, fully observable.

## Stack

- **FastAPI** — API layer
- **LiteLLM** — unified LLM gateway
- **Ollama** — local model inference
- **Langfuse** — tracing and observability

## Quick start

```bash
cp .env.example .env  # fill in Langfuse keys
docker compose -f infra/docker-compose.yml up --build
```

API + UI at `http://localhost:8000`. See [docs/setup.md](docs/setup.md) for full instructions.

## Docs

- [Architecture](docs/architecture.md)
- [Backend](docs/backend.md)
- [Routing](docs/routing.md)
- [Observability](docs/observability.md)
- [Setup](docs/setup.md)
