import logging 
import json
from flask import Blueprint, request, jsonify, current_app
# from gemini import geenrate_response


webhook_blueprint = BLueprint("webhook", __name__)


def handle_messages():
    """
    Handle incoming webhook events from the WhatsApp API.

    This function processes incoming WhatsApp messages and other events,
    such as delivery statuses. If the event is a valid message, it gets
    processed. If the incoming payload is not a recognized WhatsApp event,
    an error is returned.

    Every message send will trigger 4 HTTP requests to your webhook: message, sent, delivered, read.

    Returns:
        response: A tuple containing a JSON response and an HTTP status code.
    """
    
    body = request.get_json()
    if (body.get("entry", [{}])[0]
    .get("changes", [{}])[0]
    .get("value", {})
    .get("stasuses")
    ):
        logging.info("Received a Whatsapp status update.")
        return jsonify({"status": "ok"}), 200



VERIFY_TOKEN = "omgslay"



def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
