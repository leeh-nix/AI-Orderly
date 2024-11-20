import logging
import json
import requests
import re

from flask import current_app, jsonify
from logger import logger
from src.utils.gemini import generate_response


def log_http_response(response):
    logging.info(f"Status: {response.status_code}")
    logger(f"Status: {response.status_code}")
    logging.info(f"Content-type: {response.headers.get('content-type')}")
    logger(f"Content-type: {response.headers.get('content-type')}")
    logging.info(f"Body: {response.text}")
    logger(f"Body: {response.text}")


def get_text_message_input(recipient, text):
    return json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": recipient,
            "type": "text",
            "text": {"preview_url": False, "body": text},
        }
    )


def send_message(data):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {current_app.config['ACCESS_TOKEN']}",
    }

    url = f"https://graph.facebook.com/{current_app.config['VERSION']}/{current_app.config['PHONE_NUMBER_ID']}/messages"

    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        logger(f"Response: {response}")
        response.raise_for_status()
    except requests.Timeout:
        logging.error("Timeout occured while sending message")
        logger("Timeout occured while sending message")
        return jsonify({"status": "error", "message": "Request timed out"}), 408

    except requests.RequestException as e:
        logging.error(f"Request failed due to {e}")
        logger(f"Request failed due to {e}")
        return jsonify({"status": "error", "message": "Failed to send message"}), 500

    else:
        log_http_response(response)


def process_text_for_whatsapp(text):
    # Remove brackets
    pattern = r"\【.*?\】"
    # Substitute the pattern with an empty string
    text = re.sub(pattern, "", text).strip()

    # Pattern to find double asterisks including the word(s) in between
    pattern = r"\*\*(.*?)\*\*"

    # Replacement pattern with single asterisks
    replacement = r"*\1*"

    # Substitute occurrences of the pattern with the replacement
    whatsapp_style_text = re.sub(pattern, replacement, text)

    return whatsapp_style_text


# def process_whatsapp_message(body):
#     wa_id = body["entry"][0]["changes"][0]["value"]["contacts"][0]["wa_id"]
#     name = body["entry"][0]["changes"][0]["value"]["contacts"][0]["profile"]["name"]

#     message = body["entry"][0]["changes"][0]["value"]["messages"][0]
#     message_body = message["text"]["body"]

#     # TODO: implement custom function here
#     # response = generate_response(message_body)

#     # Gemini Integration
#     # response = generate_response(message_body, wa_id, name)
#     response = generate_response(message_body)
#     response = process_text_for_whatsapp(response)

#     data = get_text_message_input(wa_id, response)
#     logger(f"pocess_whatsapp_message:\n{data}")
#     send_message(data)


def process_whatsapp_message(body):
    wa_id = body["entry"][0]["changes"][0]["value"]["contacts"][0]["wa_id"]
    name = body["entry"][0]["changes"][0]["value"]["contacts"][0]["profile"]["name"]

    message = body["entry"][0]["changes"][0]["value"]["messages"][0]
    message_type = message["type"]  # Determine the message type

    # Handle Text Messages
    # if message_type == "text":
    message_body = message["text"]["body"]
    logging.info(f"Processing text message from {name} ({wa_id}): {message_body}")
    # logger(f"Processing text message from {name} ({wa_id}): {message_body}")

    response = generate_response(message_body)
    response = process_text_for_whatsapp(response)
    data = get_text_message_input(wa_id, response)
    send_message(data)

    # else:
    #     # Unknown message type handling
    #     logging.warning(f"Received an unknown message type from {name} ({wa_id}).")
    #     logger(f"Received an unknown message type from {name} ({wa_id}).")

    #     response = "Sorry, I didn't understand that."
    #     data = get_text_message_input(wa_id, response)
    #     send_message(data)


def is_valid_whatsapp_message(body):
    """
    Check if the incoming webhook event has a valid WhatsApp message structure.
    """
    return (
        body.get("object")
        and body.get("entry")
        and body["entry"][0].get("changes")
        and body["entry"][0]["changes"][0].get("value")
        and body["entry"][0]["changes"][0]["value"].get("messages")
        and body["entry"][0]["changes"][0]["value"]["messages"][0]
    )
