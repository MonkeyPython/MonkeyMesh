# Observability

## Provider

[Langfuse](https://langfuse.com) — traces, spans, and latency.

## Trace structure

```
trace: chat
  ├── span: router        (input: complexity, task_type, cost_sensitive)
  │                       (output: model, reason, confidence)
  └── span: llm_call      (input: model, message)
                          (output: reply, latency_ms)
```

## API

All functions are in `backend/observability/tracer.py`.

| Function | Purpose |
|---|---|
| `trace(event, data)` | Emit a structured log event |
| `start_trace(name, data)` | Start a root Langfuse trace |
| `span(trace, name, data)` | Context manager — creates a span, records latency on exit |

## Coverage

| Layer | Traced |
|---|---|
| API | `api_request` on every `/chat` call |
| Service | `chat_request`, `router_decision` |
| Router | Langfuse span with decision output |
| Gateway | `llm_call`, `llm_response`, `llm_error` |

## Configuration

Set via environment variables (see [setup.md](setup.md)):

- `LANGFUSE_PUBLIC_KEY`
- `LANGFUSE_SECRET_KEY`
- `LANGFUSE_HOST`
