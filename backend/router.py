from backend.models.requests import ChatRequest
from backend.models.responses import RouterDecision
from backend.config import settings


def route(request: ChatRequest) -> RouterDecision:
    # TODO(ml-routing): replace _rule_based_route with an ML model call once
    # enough evaluation data is collected. Keep this function as the single
    # entry point so callers never change.
    return _rule_based_route(request)


def _rule_based_route(request: ChatRequest) -> RouterDecision:
    # Cost-sensitive requests always go local unless complexity is high
    if request.cost_sensitive and request.complexity != "high":
        return RouterDecision(
            model=settings.low_complexity_model,
            reason="Cost-sensitive request routed to local model",
            confidence=0.9,
        )

    match request.complexity:
        case "low":
            return RouterDecision(
                model=settings.low_complexity_model,
                reason="Low complexity task routed to local model",
                confidence=0.95,
            )
        case "high":
            return RouterDecision(
                model=settings.high_complexity_model,
                reason="High complexity task routed to Claude",
                confidence=0.95,
            )
        case _:
            return RouterDecision(
                model=settings.medium_complexity_model,
                reason="Medium complexity task routed to Mixtral",
                confidence=0.85,
            )
