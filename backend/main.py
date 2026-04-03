from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from backend.models.requests import ChatRequest
from backend.models.responses import ChatResponse
from backend.services.chat_service import handle_chat

FRONTEND_DIR = Path(__file__).parent.parent / "frontend"

app = FastAPI(title="Monkey Mesh")

app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")


@app.get("/", include_in_schema=False)
async def index() -> FileResponse:
    return FileResponse(str(FRONTEND_DIR / "index.html"))


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    return await handle_chat(request)


@app.get("/health")
async def health() -> dict:
    return {"status": "ok"}
