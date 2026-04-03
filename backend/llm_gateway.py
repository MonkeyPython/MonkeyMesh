import litellm
from backend.models.gateway import LLMRequest, LLMResponse
from backend.observability.tracer import trace

litellm.drop_params = True


async def call_llm(request: LLMRequest) -> LLMResponse:
    # TODO(caching): before calling the model, check a cache keyed on
    # (request.model, hash(request.message)). Return cached LLMResponse on hit.
    # Use Redis or an in-memory TTL cache (e.g. cachetools.TTLCache).

    trace("llm_call", {"model": request.model, "message": request.message})

    try:
        raw = await litellm.acompletion(
            model=request.model,
            messages=[{"role": "user", "content": request.message}],
        )
        reply: str = raw.choices[0].message.content
    except Exception as exc:
        # TODO(fallback): implement a fallback chain here.
        # Example: if primary model fails, retry with settings.fallback_model.
        # Log the failure to Langfuse before re-raising.
        trace("llm_error", {"model": request.model, "error": str(exc)})
        raise

    # TODO(caching): store (request.model, hash(request.message)) → reply in cache.

    # TODO(evaluation): emit (request, reply) to an evaluation pipeline
    # (e.g. Langfuse dataset, async queue) for quality scoring.

    response = LLMResponse(model=request.model, reply=reply)
    trace("llm_response", {"model": response.model, "reply": response.reply})
    return response
