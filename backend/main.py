
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="Tech Assistant API",
    description="All-in-One Multilingual AI Assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
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
        "status": "API Ready",
        "type": "All-in-One AI"
    }

@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "user_message": request.message,
        "language": request.language,
        "reply": "AI connection is coming soon!",
        "status": "demo"
    }
  
