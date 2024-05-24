import logging
import json
import requests
import re

from .services.gemini import generate_response
from flask import current_app, jsonify


def log_http_response(response):
    logging.info(f"Status: {response.status_code}")
    logging.info(f"Content-type: {response.headers.get('content-type')}")
    logging.info(f"Body: {response.text}")

def get_text_message_input(recipient, text):
    return json.dump(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": recipient,
            "type": "text", 
            "text": {"preview_url": False, "body": text},
        }
    )

def generate_response(response):
    return response.upper()



