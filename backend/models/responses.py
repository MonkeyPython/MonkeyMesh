from pydantic import BaseModel


class RouterDecision(BaseModel):
    model: str
    reason: str
    confidence: float


class ChatResponse(BaseModel):
    reply: str
    model_used: str
    router_decision: RouterDecision
