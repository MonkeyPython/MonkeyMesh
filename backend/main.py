from fastapi import FastAPI
from backend.models.requests import ChatRequest
from backend.models.responses import ChatResponse
from backend.services.chat_service import handle_chat

app = FastAPI(title="Monkey Mesh")


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    return await handle_chat(request)


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}
