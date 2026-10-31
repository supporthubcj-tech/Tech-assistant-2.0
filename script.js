const API_URL = "http://localhost:8000";

async function sendMessage() {
    const input = document.getElementById("userInput");
    const chat = document.getElementById("chat");

    const message = input.value.trim();
    if (!message) return;

    addMessage(message, "user");
    input.value = "";

    const loading = addMessage("Thinking...", "bot");

    try {
        const response = await fetch(`${API_URL}/chat`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message,
                language: "auto",
                session_id: "default"
            })
        });

        if (!response.ok) {
            throw new Error("Backend connection failed");
        }

        const data = await response.json();
        loading.textContent = data.reply;

    } catch (error) {
        loading.textContent =
            "AI server is not connected. Please start the backend.";
    }
}

function addMessage(message, sender) {
    const chat = document.getElementById("chat");
    const div = document.createElement("div");

    div.className = `message ${sender}`;
    div.textContent = message;

    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;

    return div;
      }
