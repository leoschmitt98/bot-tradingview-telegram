
from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = 'COLE_SEU_TOKEN'
CHAT_ID = 'COLE_SEU_CHAT_ID'

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    message = data.get("message", "🚨 Sinal de entrada detectado!")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, json=payload)
    return "OK", 200

@app.route("/", methods=["GET"])
def index():
    return "Bot online!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
