from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

try:
    from .ai_engine import ask_ai
    from .database import (
        initialize_database, save_message,
        get_history, delete_history
    )
    from .memory import (
        initialize_memory, save_memory,
        get_memories, delete_memory, delete_all_memories
    )
except ImportError:
    from ai_engine import ask_ai
    from database import (
        initialize_database, save_message,
        get_history, delete_history
    )
    from memory import (
        initialize_memory, save_memory,
        get_memories, delete_memory, delete_all_memories
    )

app = FastAPI(
    title="Tech Assistant",
    description="All-in-One AI Assistant",
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
    session_id: str = "default"

class MemoryRequest(BaseModel):
    user_id: str
    memory: str

@app.on_event("startup")
def startup():
    initialize_database()
    initialize_memory()

@app.get("/")
def home():
    return {
        "name": "Tech Assistant",
        "version": "2.0.0",
        "status": "Online"
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
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    try:
        save_message(request.session_id, "user", request.message)
        reply = await ask_ai(request.message)
        save_message(request.session_id, "assistant", reply)

        return {
            "assistant": "Tech Assistant",
            "session_id": request.session_id,
            "reply": reply,
            "status": "success"
        }
    except Exception:
        raise HTTPException(
            status_code=503,
            detail="AI service unavailable. Check backend configuration."
        )

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

@app.post("/memory")
def add_memory(request: MemoryRequest):
    if not request.user_id.strip() or not request.memory.strip():
        raise HTTPException(status_code=400, detail="Missing information")

    if len(request.memory) > 1000:
        raise HTTPException(status_code=400, detail="Memory is too long")

    save_memory(request.user_id, request.memory)
    return {"status": "Memory saved"}

@app.get("/memory/{user_id}")
def view_memory(user_id: str):
    return {"memories": get_memories(user_id)}

@app.delete("/memory/{user_id}/{memory_id}")
def remove_memory(user_id: str, memory_id: int):
    if not delete_memory(user_id, memory_id):
        raise HTTPException(status_code=404, detail="Memory not found")

    return {"status": "Memory deleted"}

@app.delete("/memory/{user_id}")
def clear_memories(user_id: str):
    delete_all_memories(user_id)
    return {"status": "All memories deleted"}
