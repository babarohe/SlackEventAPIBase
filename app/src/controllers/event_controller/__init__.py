
from flask import request

from .url_verification import UrlVerification
from .event_callback import EventCallback

EVENT_TYPE_URL_VERIFICATION = "url_verification"
EVENT_TYPE_EVENT_CALLBACK = "event_callback"

class EventController(object):
    def __init__(self):
        pass

    def main(self):
        """Main process of Controller

        Returns:
            flask.Response -- Flask HTTP Response
        """
        # Choice the controller
        controller = self._selector()

        # Execution controller process
        response_object = controller.execute()

        return response_object


    def _selector(self):
        """Event selector
        Return the controller from the event type

        Returns:
            object -- Controller object
        """
        request_payload_event_type = request.json.get("type")

        if request_payload_event_type == EVENT_TYPE_URL_VERIFICATION:
            # Request type is URL verify
            controller = UrlVerification()

        elif request_payload_event_type == EVENT_TYPE_EVENT_CALLBACK:
            # Request type is event callback
            controller = EventCallback()
        else:
            # Error
            raise RuntimeError(f"'{request_payload_event_type}' is unknown event")


        return controller
