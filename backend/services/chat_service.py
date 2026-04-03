import time

from backend.models.requests import ChatRequest
from backend.models.responses import ChatResponse
from backend.router import route
from backend.llm_gateway import call_llm
from backend.observability.tracer import trace, start_trace, span


async def handle_chat(request: ChatRequest) -> ChatResponse:
    trace("chat_request", {"message": request.message, "complexity": request.complexity})

    lf_trace = start_trace(
        name="chat",
        input={"message": request.message, "complexity": request.complexity},
    )

    with span(lf_trace, "router", input={"complexity": request.complexity}) as router_span:
        decision = route(request.complexity)
        router_span.update(
            output={"model": decision.model, "reason": decision.reason, "confidence": decision.confidence}
        )

    trace("router_decision", {"model": decision.model, "reason": decision.reason})

    t0 = time.perf_counter()
    with span(lf_trace, "llm_call", input={"model": decision.model, "message": request.message}) as llm_span:
        reply = await call_llm(decision, request.message)
        latency_ms = round((time.perf_counter() - t0) * 1000, 2)
        llm_span.update(output={"reply": reply}, metadata={"latency_ms": latency_ms})

    lf_trace.update(
        output={"reply": reply, "model_used": decision.model},
        metadata={"latency_ms": latency_ms},
    )

    return ChatResponse(reply=reply, model_used=decision.model, router_decision=decision)
