import os
from certifi import contents
from flask import current_app
import requests
import dotenv

dotenv.load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL") or current_app.config.get(
    "DISCORD_WEBHOOK_URL"
)

def logger(content, log_type: str = "info"):
    """
    Sends a message to a Discord channel using a webhook.

    :param content: The message content to send.
    """
    if not DISCORD_WEBHOOK_URL:
        print("Discord Webhook URL is not set correctly.")
        return

    print(f"Discord Webhook URL: {DISCORD_WEBHOOK_URL}")

    data = {
        "content": "",
        "embeds": [
            {
                "type": "rich",
                "title": log_type.capitalize(),
                "description": content,
                "color": 0x0000FF if log_type == "info" else 0xFF0000,
            }
        ],
    }

    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=data)
        if response.status_code == 204:
            print("Webhook sent successfully!")
        else:
            print(
                f"Failed to send webhook. Status code: {response.status_code}, Response: {response.text}"
            )
    except requests.RequestException as e:
        print(f"Failed to send webhook due to exception: {e}")