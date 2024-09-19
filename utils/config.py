import os
import dotenv
from flask import Flask


def load_configurations(app: Flask) -> None:
    """
    Load environment variables from .env file and set them as configuration
    options on the given Flask app.

    The following environment variables are expected to be set:

    * ACCESS_TOKEN: The Facebook access token to use for interacting with the
      WhatsApp Business API.
    * YOUR_PHONE_NUMBER: The phone number associated with your WhatsApp
      Business account.
    * APP_ID: The ID of your Facebook Developer app.
    * APP_SECRET: The secret key associated with your Facebook Developer app.
    * RECIPIENT_WAID: The WhatsApp ID of the person you want to send messages to.
    * VERSION: The version of the WhatsApp Business API to use.
    * PHONE_NUMBER_ID: The ID of your WhatsApp Business phone number.
    * VERIFY_TOKEN: The verification token provided by the WhatsApp Business API
      when you set up your webhook.
    * DISCORD_WEBHOOK_URL: The URL of the Discord webhook to use for sending
      messages.

    :param app: The Flask app to set the configuration options on.
    :type app: Flask
    """
    dotenv.load_dotenv()
    app.config["ACCESS_TOKEN"] = os.getenv("ACCESS_TOKEN")
    app.config["YOUR_PHONE_NUMBER"] = os.getenv("YOUR_PHONE_NUMBER")
    app.config["APP_ID"] = os.getenv("APP_ID")
    app.config["APP_SECRET"] = os.getenv("APP_SECRET")
    app.config["RECIPIENT_WAID"] = os.getenv("RECIPIENT_WAID")
    app.config["VERSION"] = os.getenv("VERSION")
    app.config["PHONE_NUMBER_ID"] = os.getenv("PHONE_NUMBER_ID")
    app.config["VERIFY_TOKEN"] = os.getenv("VERIFY_TOKEN")
    app.config["DISCORD_WEBHOOK_URL"] = os.getenv("DISCORD_WEBHOOK_URL")
    app.config["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
