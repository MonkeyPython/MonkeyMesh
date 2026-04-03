import litellm
from backend.models.responses import RouterDecision
from backend.observability.tracer import trace

litellm.drop_params = True


async def call_llm(decision: RouterDecision, message: str) -> str:
    trace("llm_call", {"model": decision.model, "message": message})

    response = await litellm.acompletion(
        model=decision.model,
        messages=[{"role": "user", "content": message}],
    )

    reply: str = response.choices[0].message.content
    trace("llm_response", {"model": decision.model, "reply": reply})
    return reply
