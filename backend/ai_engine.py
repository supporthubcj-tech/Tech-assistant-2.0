
import os
import httpx

AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL", "gemini-2.5-flash"
)

OLLAMA_URL = os.getenv(
    "OLLAMA_URL", "http://localhost:11434"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL", "qwen3:4b"
)

SYSTEM_PROMPT = """
You are Tech Assistant, an all-in-one AI assistant.

You must:
- Understand all languages.
- Reply in the user's language.
- Help with general knowledge.
- Help with IT and computer problems.
- Help with programming and coding.
- Help with education and mathematics.
- Help with writing and translation.
- Explain difficult topics simply.
- Never pretend to have searched the web.
- Be accurate, helpful and friendly.
"""

async def ask_ai(message: str):

    async with httpx.AsyncClient(timeout=90) as client:

        if AI_PROVIDER == "ollama":

            response = await client.post(
                f"{OLLAMA_URL}/api/chat",
                json={
                    "model": OLLAMA_MODEL,
                    "messages": [
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": message}
                    ],
                    "stream": False
                }
            )

            response.raise_for_status()
            data = response.json()

            return data["message"]["content"]

        elif AI_PROVIDER == "gemini":

            if not GEMINI_API_KEY:
                raise ValueError("Gemini API key is missing")

            response = await client.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent",
                headers={
                    "x-goog-api-key": GEMINI_API_KEY
                },
                json={
                    "system_instruction": {
                        "parts": [{"text": SYSTEM_PROMPT}]
                    },
                    "contents": [{
                        "parts": [{"text": message}]
                    }]
                }
            )

            response.raise_for_status()
            data = response.json()

            return data["candidates"][0]["content"]["parts"][0]["text"]

        else:
            raise ValueError("Invalid AI provider")
