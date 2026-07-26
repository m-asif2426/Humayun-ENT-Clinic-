from fastapi import APIRouter
from models import ChatRequest, ChatResponse
from services.chat_service import get_response

router = APIRouter(tags=["Chat"])


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    FAQ-based chatbot endpoint.
    Returns a keyword-matched answer or a helpful fallback.
    Replace `get_response()` with an AI call (Gemini / OpenAI) when ready.
    """
    reply = get_response(request.message)
    return ChatResponse(reply=reply)
