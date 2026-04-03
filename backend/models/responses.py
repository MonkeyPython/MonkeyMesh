from pydantic import BaseModel
from backend.models.routing import RouterDecision


class ChatResponse(BaseModel):
    reply: str
    model_used: str
    router_decision: RouterDecision
