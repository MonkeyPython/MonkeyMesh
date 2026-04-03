from pydantic import BaseModel


class LLMRequest(BaseModel):
    model: str
    message: str


class LLMResponse(BaseModel):
    model: str
    reply: str
