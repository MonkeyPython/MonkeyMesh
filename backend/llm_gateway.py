from backend.models.responses import RouterDecision
from backend.observability.tracer import trace


async def call_llm(decision: RouterDecision, message: str) -> str:
    trace("llm_call", {"model": decision.model, "message": message})
    # litellm integration point
    raise NotImplementedError("litellm integration not yet wired")
