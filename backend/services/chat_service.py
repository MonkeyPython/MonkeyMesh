from backend.models.requests import ChatRequest
from backend.models.responses import ChatResponse
from backend.router import route
from backend.llm_gateway import call_llm
from backend.observability.tracer import trace


async def handle_chat(request: ChatRequest) -> ChatResponse:
    trace("chat_request", {"message": request.message, "complexity": request.complexity})

    decision = route(request.complexity)
    trace("router_decision", {"model": decision.model, "reason": decision.reason})

    reply = await call_llm(decision, request.message)

    return ChatResponse(reply=reply, model_used=decision.model, router_decision=decision)
