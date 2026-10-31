
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CJ Tech Assistant 2.0</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <aside class="sidebar">
    <h2>✦ CJ Tech</h2>
    <button onclick="newChat()">+ New Chat</button>
    <h4>CHAT HISTORY</h4>
    <div id="history"></div>
    <p>Version 2.0</p>
  </aside>

  <main>
    <header>
      <button onclick="toggleMenu()">☰</button>
      <h3>CJ Tech Assistant <span>2.0</span></h3>
      <button onclick="toggleTheme()">☼</button>
    </header>

    <section id="chat">
      <div class="welcome" id="welcome">
        <div class="logo">✦</div>
        <h1>How can I help you?</h1>
        <p>Your Personal AI Assistant</p>
        <div class="cards">
          <button onclick="quickAsk('Help me with Windows troubleshooting')">🖥 IT Support</button>
          <button onclick="quickAsk('Help me write code')">💻 Coding</button>
          <button onclick="quickAsk('Teach me something')">📚 Learning</button>
          <button onclick="quickAsk('Help me write an email')">✍ Writing</button>
        </div>
      </div>
      <div id="messages"></div>
    </section>

    <footer>
      <select id="mode">
        <option>General</option>
        <option>IT Support</option>
        <option>Coding</option>
        <option>Learning</option>
        <option>Writing</option>
      </select>
      <textarea id="prompt" placeholder="Message CJ Tech Assistant..."></textarea>
      <button onclick="sendMessage()">➤</button>
    </footer>
    <p class="note">AI responses require backend connection. Verify important information.</p>
  </main>

  <script src="script.js"></script>
</body>
</html>
