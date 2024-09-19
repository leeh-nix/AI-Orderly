from flask import Flask
from flask_restful import Api
from utils.logger import configure_logging
from utils.config import load_configurations
import google.generativeai as genai


class BaseAPIClass(Api):
    def __init__(self, app: Flask, **kwargs) -> None:
        super().__init__(app)
        self.app = app
        self.gemini = None
        self.configs(**kwargs)
        self.initialize_gemini()
        self.app.generate_response = self.generate_response

    def configs(self, **kwargs) -> None:
        """
        Configure the API with given keyword arguments.

        Loads configuration from the .env file using load_configurations,
        sets up logging with configure_logging, and then overrides any
        configuration settings with the given keyword arguments.

        :param kwargs: Configuration settings to override.
        :type kwargs: dict
        """
        load_configurations(self.app)
        configure_logging()
        for config, value in kwargs:
            self.app.config[config.upper()] = value

    def initialize_gemini(self) -> None:
        """
        Initialize the Gemini API with the configured API key.

        This method is called during the initialization of the API and sets up
        the Gemini API client with the configured API key. It also sets up the
        model object with the name "gemini-1.5-flash-latest".
        """
        genai.configure(api_key=self.app.config["GEMINI_API_KEY"])
        model_pro = genai.GenerativeModel(
            model_name="gemini-1.5-flash-latest",
        )
        self.gemini = model_pro
        self.app.gemini = self.gemini
        self.app.generate_response = self.generate_response
        return

    def generate_response(self, text: str) -> str:
        """
        Generates a response based on the given text.

        Args:
            text (str): The input text to generate a response from.

        Returns:
            str: The generated response.

        """
        response = self.gemini.generate_content(
            contents=text,
        )
        return response.text

    def register_resource(self, resource, *args, **kwargs) -> None:
        """
        Registers a resource to the API.

        This method is a simple wrapper around the
        :meth:`flask_restful.Api.add_resource` method.

        :param resource: The resource to add to the API.
        :type resource: flask_restful.Resource
        :param args: Additional positional arguments to pass to the
            :meth:`flask_restful.Api.add_resource` method.
        :type args: tuple
        :param kwargs: Additional keyword arguments to pass to the
            :meth:`flask_restful.Api.add_resource` method.
        :type kwargs: dict
        """
        return self.add_resource(resource, *args, **kwargs)

    def run(self, **kwargs) -> None:
        """
        Runs the Flask application.

        This method is a simple wrapper around the
        :meth:`flask.Flask.run` method.

        :param kwargs: Additional keyword arguments to pass to the
            :meth:`flask.Flask.run` method.
        :type kwargs: dict
        """
        return self.app.run(**kwargs)
