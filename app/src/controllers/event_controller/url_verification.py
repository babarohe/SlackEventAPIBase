
from .controller_base import _EventControllerBase

class UrlVerification(_EventControllerBase):
    def __init__(self):
        super().__init__()

    def execute(self):
        # Get the challenge key
        request_payload_challenge = self.get_request_payload("challenge")

        # Create response data
        response_data = {
            "challenge": request_payload_challenge
        }

        # Build of response data
        response_object = self.build_response_application_json(response_data)

        return response_object
