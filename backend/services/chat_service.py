import time

from backend.models.requests import ChatRequest
from backend.models.responses import ChatResponse
from backend.models.gateway import LLMRequest
from backend.router import route
from backend.llm_gateway import call_llm
from backend.observability.tracer import trace, start_trace, span


async def handle_chat(request: ChatRequest) -> ChatResponse:
    # TODO(caching): compute a cache key here from (message, complexity,
    # task_type) and return a cached ChatResponse early on hit.

    trace("chat_request", {
        "message": request.message,
        "task_type": request.task_type,
        "complexity": request.complexity,
        "cost_sensitive": request.cost_sensitive,
    })

    lf_trace = start_trace(
        name="chat",
        input={
            "message": request.message,
            "task_type": request.task_type,
            "complexity": request.complexity,
            "cost_sensitive": request.cost_sensitive,
        },
    )

    with span(lf_trace, "router", input={
        "complexity": request.complexity,
        "task_type": request.task_type,
        "cost_sensitive": request.cost_sensitive,
    }) as router_span:
        decision = route(request)
        router_span.update(
            output={"model": decision.model, "reason": decision.reason, "confidence": decision.confidence}
        )

    trace("router_decision", {"model": decision.model, "reason": decision.reason})

    llm_request = LLMRequest(model=decision.model, message=request.message)

    t0 = time.perf_counter()
    with span(lf_trace, "llm_call", input={"model": llm_request.model, "message": llm_request.message}) as llm_span:
        llm_response = await call_llm(llm_request)
        latency_ms = round((time.perf_counter() - t0) * 1000, 2)
        llm_span.update(output={"reply": llm_response.reply}, metadata={"latency_ms": latency_ms})

    lf_trace.update(
        output={"reply": llm_response.reply, "model_used": llm_response.model},
        metadata={"latency_ms": latency_ms},
    )

    # TODO(evaluation): after returning, push (request, llm_response, decision)
    # to an async evaluation queue for human or automated quality review.

    return ChatResponse(reply=llm_response.reply, model_used=llm_response.model, router_decision=decision)
