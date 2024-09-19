import json
import logging
from utils.logger import logger
from flask import current_app, jsonify, request
from requests import Response
from utils.whatsapp import is_valid_whatsapp_message, process_whatsapp_message
from utils.bassendpointclass import BaseEndpointClass


class WebhookEndpoint(BaseEndpointClass):
    def get(self) -> None:
        """
        Handle GET requests to the webhook endpoint.

        Returns a JSON response with the verification token sent by the
        WhatsApp Business API to verify the webhook.
        """
        logger("Verifying!")
        return self.verify()

    def post(self) -> None:
        return self.handle_message()

    def verify(self):
        """
        Handle the webhook verification request sent by the WhatsApp Business API.

        Returns a JSON response with the challenge token sent in the request if
        the verification token and mode are correct.

        Args:
            mode (str): The mode parameter sent in the request.
            token (str): The verification token sent in the request.
            challenge (str): The challenge token sent in the request.

        Returns:
            tuple: A tuple containing the response and status code.

        Raises:
            HTTPException: If the verification token and mode are incorrect.

        """
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if mode and token:
            if mode == "subscribe" and token == current_app.config["VERIFY_TOKEN"]:
                logging.info("WEBHOOK_VERIFIED")
                logger("WEBHOOK_VERIFIED")
                return challenge, 200
            else:
                logging.info("VERIFICATION_FAILED")
                logger("VERIFICATION_FAILED")
                return jsonify(
                    {"status": "error", "message": "Verification failed"}
                ), 403
        else:
            logging.info("MISSING_PARAMETER")
            logger("MISSING_PARAMETER")
            return jsonify({"status": "error", "message": "Missing parameters"}), 400

    def handle_message(self) -> Response:
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
        logger(body)
        if body is not None:
            if (
                body.get("entry", [{}])[0]
                .get("changes", [{}])[0]
                .get("value", {})
                .get("stasuses")
            ):
                logging.info("Received a Whatsapp status update.")
                logger("Received a Whatsapp status update.")
                return jsonify({"status": "ok"}), 200
        try:
            if is_valid_whatsapp_message(body):
                process_whatsapp_message(body)
                return jsonify({"status": "ok"}), 200
            else:
                return (
                    jsonify({"status": "error", "message": "Not a WhatsApp API event"}),
                    404,
                )
        except json.JSONDecodeError:
            logging.error("Failed to decode JSON")
            return jsonify({"status": "error", "message": "Invalid JSON provided"}), 400
