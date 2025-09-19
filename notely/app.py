from flask import Flask, jsonify
import os

app = Flask(__name__)  # Erstellt eine Flask-App-Instanz

# Lies den Projektnamen aus der Umgebungsvariable (Fallback: "notely")
PROJECT_ID = os.getenv("PROJECT_ID", "notely")

@app.get("/health")
def health():
    return jsonify(status="ok", project=PROJECT_ID)

@app.get("/")
def index():
    return jsonify(app="notely", message="Hallo von Docker + ngrok!", project=PROJECT_ID)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))  # Lies den Port aus .env (Fallback 8080)
    app.run(host="0.0.0.0", port=port)

