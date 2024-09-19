import sys
import logging
import requests
from flask import current_app


def configure_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
    )


def logger(content):
    """
    Sends a message to a Discord channel using a webhook.

    :param content: The message content to send.
    """
    DISCORD_WEBHOOK_URL = current_app.config.get("DISCORD_WEBHOOK_URL")

    if not DISCORD_WEBHOOK_URL:
        print("Discord Webhook URL is not set correctly.")
        return

    print(f"Discord Webhook URL: {DISCORD_WEBHOOK_URL}")

    data = {
        "content": content,
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
