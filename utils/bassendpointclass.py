from flask_restful import Resource


class BaseEndpointClass(Resource):
    """
    Base class for creating API endpoints.
    """

    def get(self) -> None:
        """
        Handle a GET request to the endpoint.

        This method is a stub and must be overridden by any subclass.

        Returns:
            response: A tuple containing a JSON response and an HTTP status code.
        """

        pass

    def post(self) -> None:
        """
        Handle a POST request to the endpoint.

        This method is a stub and must be overridden by any subclass.

        Returns:
            response: A tuple containing a JSON response and an HTTP status code.
        """
        pass

    def put(self) -> None:
        """
        Handle a PUT request to the endpoint.

        This method is a stub and must be overridden by any subclass.

        Returns:
            response: A tuple containing a JSON response and an HTTP status code.
        """

        pass

    def delete(self) -> None:
        """
        Handle a DELETE request to the endpoint.

        This method is a stub and must be overridden by any subclass.

        Returns:
            response: A tuple containing a JSON response and an HTTP status code.
        """
        pass
