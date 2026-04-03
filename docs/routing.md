# Routing

## Input

```python
class ChatRequest(BaseModel):
    message: str
    task_type: str = "general"
    complexity: Literal["low", "medium", "high"] = "medium"
    cost_sensitive: bool = False
```

## Output

```python
class RouterDecision(BaseModel):
    model: str
    reason: str
    confidence: float
```

## Rules

| Condition | Model |
|---|---|
| `cost_sensitive=true` + complexity ≠ `high` | `ollama/mistral` (local) |
| `complexity=low` | `ollama/mistral` (local) |
| `complexity=medium` | `mistral/mixtral-8x7b-instruct` |
| `complexity=high` | `anthropic/claude-3-5-sonnet-20241022` |

## Model strings (litellm)

| Alias | litellm string |
|---|---|
| Local | `ollama/mistral` |
| Medium | `mistral/mixtral-8x7b-instruct` |
| High / Claude | `anthropic/claude-3-5-sonnet-20241022` |

Models are configured in `backend/config.py` and overridable via `Settings`.

## Extensibility

`route()` in `router.py` is the single entry point.  
To swap to ML-based routing, replace `_rule_based_route` — callers never change.
