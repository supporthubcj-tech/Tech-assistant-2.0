
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from ai_engine import ask_ai

app = FastAPI(
    title="Tech Assistant",
    description="All-in-One Hybrid AI Assistant",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

class ChatRequest(BaseModel):
    message: str
    language: str = "auto"

@app.get("/")
def home():
    return {
        "name": "Tech Assistant",
        "version": "2.0.0",
        "status": "Online",
        "engine": "Hybrid AI"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "time": datetime.now().isoformat()
    }

@app.post("/chat")
async def chat(request: ChatRequest):

    if not request.message.strip():
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty"
        )

    try:
        reply = await ask_ai(request.message)

        return {
            "assistant": "Tech Assistant",
            "reply": reply,
            "language": request.language,
            "status": "success"
        }

    except Exception as error:
        raise HTTPException(
            status_code=503,
            detail="AI service unavailable. Check provider configuration."
        )

@app.get("/features")
def features():
    return {
        "general_ai": True,
        "multilingual": True,
        "it_support": True,
        "coding": True,
        "translation": True,
        "writing": True,
        "voice": "planned",
        "web_search": "planned",
        "image_generation": "planned",
        "file_reader": "planned",
        "smart_memory": "planned",
        "chat_history": "planned",
        "admin_panel": "planned"
    }
from database import (
    initialize_database,
    save_message,
    get_history,
    delete_history
)
import uuid
@app.on_event("startup")
def startup():
    initialize_database() use
    
@app.post("/chat")
async def chat(request: ChatRequest):

    if not request.message.strip():
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty"
        )

    session_id = request.session_id

    try:
        save_message(
            session_id, "user", request.message
        )

        reply = await ask_ai(request.message)

        save_message(
            session_id, "assistant", reply
        )

        return {
            "assistant": "Tech Assistant",
            "session_id": session_id,
            "reply": reply,
            "status": "success"
        }

    except Exception:
        raise HTTPException(
            status_code=503,
            detail="AI service unavailable"
        )
        session_id: str = "default"
        
@app.get("/history/{session_id}")
def history(session_id: str):
    return {
        "session_id": session_id,
        "messages": get_history(session_id)
    }

@app.delete("/history/{session_id}")
def clear_history(session_id: str):
    delete_history(session_id)
    return {"status": "History deleted"}
    
