async function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value;
    const language = document.getElementById("languageSelect").value;
    if (!message) return;
    const chatbox = document.getElementById("chatbox");
    chatbox.innerHTML += `<div><b>You:</b> ${message}</div>`;
    input.value = "";

    const response = await fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message, language })
    });
    const data = await response.json();
    chatbox.innerHTML += `<div><b>Jiraya:</b> ${data.response}</div>`;
    chatbox.scrollTop = chatbox.scrollHeight;
}

// Knowledge upload
async function uploadKnowledge() {
    const fileInput = document.getElementById("knowledgeFile");
    if (fileInput.files.length == 0) return;
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("/upload", {
        method: "POST",
        body: formData
    });
    const data = await response.json();
    alert("Uploaded: " + data.filename);
}
