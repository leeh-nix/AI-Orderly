import json
import logging
import re
import requests
from utils import logger
from flask import current_app, jsonify
from requests import Response


def log_http_response(response: Response) -> None:
    """
    Log an HTTP response's status, content-type and body.

    :param response: The HTTP response to log.
    :type response: requests.Response
    """
    logging.info(f"Status: {response.status_code}")
    logger(f"Status: {response.status_code}")
    logging.info(f"Content-type: {response.headers.get('content-type')}")
    logger(f"Content-type: {response.headers.get('content-type')}")
    logging.info(f"Body: {response.text}")
    logger(f"Body: {response.text}")


def get_text_message_input(recipient: str, text: str) -> str:
    """
    Return a JSON string representing a WhatsApp Business API message object.

    :param recipient: The phone number of the recipient to send the message to.
    :type recipient: str
    :param text: The text to send in the message.
    :type text: str
    :return: A JSON string representing a WhatsApp Business API message object.
    :rtype: str
    """
    return json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": recipient,
            "type": "text",
            "text": {"preview_url": False, "body": text},
        }
    )


def send_message(data: str) -> tuple[Response, int]:
    """
    Send a message to the WhatsApp Business API.

    :param data: A JSON string representing a WhatsApp Business API message object.
    :type data: str
    :return: A JSON response and an HTTP status code.
    :rtype: tuple[flask.Response, int]
    """
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
    pass


def process_text_for_whatsapp(text: str) -> str:
    """
    Process a text message to conform to the WhatsApp Business API.

    The following transformations are applied:

    * Remove all occurrences of  (brackets)
    * Replace all occurrences of **word** with *word*

    :param text: The text message to process.
    :type text: str
    :return: The processed text message.
    :rtype: str
    """
    pattern = r"\【.*?\】"
    text = re.sub(pattern, "", text).strip()
    pattern = r"\*\*(.*?)\*\*"
    replacement = r"*\1*"
    whatsapp_style_text = re.sub(pattern, replacement, text)

    return whatsapp_style_text


def process_whatsapp_message(body) -> None:
    """
    Process an incoming message from WhatsApp.

    :param body: The request body sent by the WhatsApp Business API.
    :type body: dict

    :return: None
    :rtype: None
    """

    wa_id = body["entry"][0]["changes"][0]["value"]["contacts"][0]["wa_id"]
    # name = body["entry"][0]["changes"][0]["value"]["contacts"][0]["profile"]["name"]

    message = body["entry"][0]["changes"][0]["value"]["messages"][0]
    message_body = message["text"]["body"]

    # TODO: implement custom function here
    # response = generate_response(message_body)

    # Gemini Integration
    # response = generate_response(message_body, wa_id, name)
    response = current_app.generate_response(message_body)
    response = process_text_for_whatsapp(response)

    data = get_text_message_input(wa_id, response)
    logger(f"pocess_whatsapp_message:\n{data}")
    send_message(data)


def is_valid_whatsapp_message(body) -> bool:
    """
    Check if the incoming webhook event has a valid WhatsApp message structure.

    :param body: The request body sent by the WhatsApp Business API.
    :type body: dict

    :return: True if the message structure is valid, False otherwise.
    :rtype: bool
    """
    return (
        body.get("object")
        and body.get("entry")
        and body["entry"][0].get("changes")
        and body["entry"][0]["changes"][0].get("value")
        and body["entry"][0]["changes"][0]["value"].get("messages")
        and body["entry"][0]["changes"][0]["value"]["messages"][0]
    )
