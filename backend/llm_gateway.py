import litellm
from backend.models.responses import RouterDecision
from backend.observability.tracer import trace

litellm.drop_params = True


async def call_llm(decision: RouterDecision, message: str) -> str:
    # TODO(caching): before calling the model, check a cache keyed on
    # (decision.model, hash(message)). Return cached reply on hit.
    # Use Redis or an in-memory TTL cache (e.g. cachetools.TTLCache).

    trace("llm_call", {"model": decision.model, "message": message})

    try:
        response = await litellm.acompletion(
            model=decision.model,
            messages=[{"role": "user", "content": message}],
        )
        reply: str = response.choices[0].message.content
    except Exception as primary_exc:
        # TODO(fallback): implement a fallback chain here.
        # Example: if primary model fails, retry with settings.fallback_model.
        # Log the failure to Langfuse before re-raising.
        trace("llm_error", {"model": decision.model, "error": str(primary_exc)})
        raise

    # TODO(caching): store (decision.model, hash(message)) → reply in cache.

    # TODO(evaluation): emit (message, reply, decision.model) to an evaluation
    # pipeline (e.g. Langfuse dataset, async queue) for quality scoring.

    trace("llm_response", {"model": decision.model, "reply": reply})
    return reply
