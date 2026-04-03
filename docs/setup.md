# Setup

## Requirements

- Python 3.11+
- [Ollama](https://ollama.ai) running locally (for low/medium complexity models)
- Langfuse account (for tracing)

## Install

```bash
pip install -r requirements.txt
```

## Environment variables

| Variable | Required | Default | Description |
|---|---|---|---|
| `LANGFUSE_PUBLIC_KEY` | Yes | — | Langfuse project public key |
| `LANGFUSE_SECRET_KEY` | Yes | — | Langfuse project secret key |
| `LANGFUSE_HOST` | No | `https://cloud.langfuse.com` | Langfuse host |

## Run

```bash
uvicorn backend.main:app --reload
```

API available at `http://localhost:8000`.
UI available at `http://localhost:8000/`.

## Local models (Ollama)

```bash
ollama pull mistral
```
