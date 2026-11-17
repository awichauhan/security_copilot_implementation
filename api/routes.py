from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse

from api.models import ChatRequest, ChatResponse
from llm.ollama import generate_response

# A router groups endpoints so main.py can stay small.
router = APIRouter()


@router.get("/")
async def home():
    # routes.py is inside api/, so go up one folder to find index.html.
    return FileResponse(Path(__file__).resolve().parent.parent / "index.html")


# response_model tells FastAPI the shape of the JSON we return.
@router.post("/api/prompt", response_model=ChatResponse)
async def generate(body: ChatRequest) -> ChatResponse:
    # Pass the prompt to the Ollama client and wait for the answer.
    answer = await generate_response(body.prompt)
    return ChatResponse(response=answer, sources=[])
