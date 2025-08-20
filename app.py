from flask import Flask, render_template, request, jsonify
from freewill import FreeWill
from utils import chat_with_openai
from vault.vault_utils import encrypt_note, decrypt_note
import os

app = Flask(__name__)
freewill = FreeWill()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message")
    language = request.json.get("language", None)
    memory = freewill.get_memory()
    context = ""
    for convo in memory[-5:]:
        context += f"User: {convo['user']}\nAI: {convo['ai']}\n"
    context += f"User: {user_input}\nAI:"

    ai_response = chat_with_openai(context, language)
    freewill.remember(user_input, ai_response)
    return jsonify({"response": ai_response})

# Knowledge upload placeholder
@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files['file']
    path = os.path.join("knowledge", file.filename)
    file.save(path)
    return jsonify({"status": "uploaded", "filename": file.filename})

# Vault endpoints placeholder
@app.route("/vault/save", methods=["POST"])
def save_note():
    data = request.json
    encrypt_note(data["text"], data["filename"])
    return jsonify({"status": "saved"})

@app.route("/vault/read/<filename>", methods=["GET"])
def read_note(filename):
    text = decrypt_note(filename)
    return jsonify({"text": text})

# Plugin system placeholder
@app.route("/plugin/<plugin_name>", methods=["POST"])
def plugin_call(plugin_name):
    return jsonify({"status": "called", "plugin": plugin_name})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
