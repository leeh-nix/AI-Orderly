import os
from flask import current_app
import requests
import dotenv

dotenv.load_dotenv()
# Replace with your actual webhook URL

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
# DISCORD_WEBHOOK_URL = current_app.config["DISCORD_WEBHOOK_URL"]


def logger(content):
    """
    Sends a message to a Discord channel using a webhook.

    :param content: The message content to send.
    """
    data = {
        "content": content,  # The message content
        # "username": "Webhook Bot",  # Optional: Set a username for the bot
    }

    # Sending the message using the webhook
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)  # type: ignore

    # Checking if the request was successful
    if response.status_code == 204:
        print("Webhook sent successfully!")
    else:
        print(
            f"Failed to send webhook. Status code: {response.status_code}, Response (webhook): {response.text}"
        )
