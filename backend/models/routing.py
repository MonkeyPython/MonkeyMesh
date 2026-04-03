from pydantic import BaseModel


class RouterDecision(BaseModel):
    model: str
    reason: str
    confidence: float
