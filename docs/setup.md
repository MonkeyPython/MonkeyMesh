# Setup

## Requirements

- Docker + Docker Compose
- Langfuse account (for tracing)

## Environment variables

Create a `.env` file at the project root:

```env
LANGFUSE_PUBLIC_KEY=your_public_key
LANGFUSE_SECRET_KEY=your_secret_key
LANGFUSE_HOST=https://cloud.langfuse.com  # optional
```

## Run with Docker Compose

```bash
docker compose -f infra/docker-compose.yml up --build
```

- API + UI: `http://localhost:8000`
- Ollama: `http://localhost:11434`

## Pull local models (first time)

```bash
docker compose -f infra/docker-compose.yml exec ollama ollama pull mistral
```

## Run without Docker (development)

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

Requires Ollama running locally on port `11434`.
