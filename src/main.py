import os
from flask import Flask, request, jsonify, send_file
import requests
# from gemini import sendResponse


app = Flask(__name__)

# DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
VERIFY_TOKEN = "omgslay"

@app.route("/", methods=['GET', 'POST'])
def name(req, res):
    print(req.body)
    return "Hello World"

@app.route("/webhook", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        verify_token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if verify_token == VERIFY_TOKEN:
            return challenge
        else:
            return 'Invalid verification token', 403
    elif request.method == 'POST':
        data = request.get_json()
        print("Received webhook data:", data)
        # Here you can process the incoming message data

        # Get response from Gemini API
        # response_text = sendResponse(user_message)
        # Send response to Discord
        # send_message_to_discord(response_text)

        return jsonify({'status': 'success'}), 200

    return send_file('index.html')


def send_message_to_discord(message):
    payload = {"content": message}
    headers = {"Content-Type": "application/json"}
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload, headers=headers)
    return response


def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
