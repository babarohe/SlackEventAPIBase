
import math
import logging

from .controller_base import _EventControllerBase

class EventCallback(_EventControllerBase):
    def __init__(self):
        super().__init__()

    def execute(self):
        # Get event
        request_payload_event       = self.get_request_payload("event")

        # Get event subtype
        request_payload_subtype     = request_payload_event.get("subtype")

        # Create response data
        response_data = {
            "status": "ok"
        }

        # Create response data
        response_object = self.build_response_application_json(response_data)

        return response_object
