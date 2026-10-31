
const chat = document.getElementById("chat");
const input = document.getElementById("userInput");

function addMessage(message, type) {
  const div = document.createElement("div");
  div.className = "message " + type;
  div.textContent = message;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

function getAIResponse(message) {
  const text = message.toLowerCase();

  if (text.includes("hello") || text.includes("hi")) {
    return "Hello! 👋 Welcome to Tech Assistant. How can I help you?";
  }

  if (text.includes("your name")) {
    return "I am Tech Assistant, your personal AI assistant.";
  }

  if (text.includes("dns")) {
    return "DNS means Domain Name System. It converts domain names into IP addresses.";
  }

  if (text.includes("dhcp")) {
    return "DHCP automatically assigns IP addresses to devices in a network.";
  }

  if (text.includes("ip address")) {
    return "An IP address is a unique network address assigned to a device.";
  }

  if (text.includes("ping")) {
    return "Ping is used to test network connectivity between devices.";
  }

  if (text.includes("windows")) {
    return "I can help with Windows installation, troubleshooting, drivers and system errors.";
  }

  if (text.includes("thank")) {
    return "You're welcome! 😊";
  }

  return "I received your question! I am currently running in basic demo mode. AI API connection will be added in the next development stage.";
}

function sendMessage() {
  const message = input.value.trim();

  if (!message) return;

  addMessage(message, "user");
  input.value = "";

  setTimeout(() => {
    const response = getAIResponse(message);
    addMessage(response, "bot");
  }, 500);
}

input.addEventListener("keydown", function(event) {
  if (event.key === "Enter") {
    sendMessage();
  }
});
      
