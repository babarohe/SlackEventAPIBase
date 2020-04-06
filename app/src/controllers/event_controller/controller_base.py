
import re
import json

from flask import Response, request

CONTENT_TYPE_APPLICATION_JSON = {"Content-Type": "application/json"}

class _EventControllerBase(object):
    def __init__(self):
        self.request_header_content_type = self.get_request_header("Content-Type")

    def get_request_header(self, key, default=None):
        """Inquiry the request header

        Arguments:
            key {str} -- Dictionaly key

        Keyword Arguments:
            default {any} -- Default value if not set (default: {None})

        Returns:
            str -- Request header value
        """
        return request.headers.get(key, default)

    def get_request_payload(self, key, default=None):
        """Inquiry the payload data

        Arguments:
            key {str} -- Dictionaly key

        Keyword Arguments:
            default {any} -- Default value if not set (default: {None})

        Raises:
            RuntimeError: Unsupported Content-Type

        Returns:
            any -- Request paylaod data
        """
        if re.match("application/json;?.*", self.request_header_content_type):
            return request.json.get(key, default)

        else:
            raise RuntimeError("Unsupported Content-Type")


    def build_response_application_json(self, data, status=200, headers={}):
        """Build application/json type response

        Arguments:
            data {dict} -- Response payload data

        Keyword Arguments:
            status {int} -- HTTP status code (default: {200})
            headers {dict} -- Respons headers (default: {{}})

        Returns:
            flask.Response -- Flask HTTP Responses
        """
        # Set the Content-Type
        headers.update(CONTENT_TYPE_APPLICATION_JSON)

        # Create jsonify data
        jsonify_payload = json.dumps(data)

        # Make response and return it
        return Response(jsonify_payload, status=200, headers=headers)
