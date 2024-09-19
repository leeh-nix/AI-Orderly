from flask import Flask
from endpoints.webhook import WebhookEndpoint
from utils.bassapiclass import BaseAPIClass

flask_app = Flask(__name__)
app = BaseAPIClass(flask_app)

app.register_resource(WebhookEndpoint, "/webhook")

if __name__ == "__main__":
    app.run(debug=True)
