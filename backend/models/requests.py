from typing import Literal
from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    task_type: str = "general"
    complexity: Literal["low", "medium", "high"] = "medium"
    cost_sensitive: bool = False
