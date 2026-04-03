from backend.models.responses import RouterDecision
from backend.config import settings


def route(complexity: str) -> RouterDecision:
    match complexity:
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
