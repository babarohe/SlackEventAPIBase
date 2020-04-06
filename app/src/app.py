#!/usr/bin/env python

import os
import logging
import json
import pprint

from flask import Flask, request, Response

from controllers.event_controller import EventController
from configuration import config

app = Flask(__name__)


# Set logging level to the root logger
if config.FLASK_DEBUG == "DEBUG":
    logging_level = logging.DEBUG
else:
    logging_level = logging.INFO

# Initialize root logger
logging.basicConfig(level=logging.DEBUG, format="<%(levelname)s> %(asctime)s: %(message)s")


@app.route('/slack/event/callback', methods=['POST'])
def slack_event():
    """First controller to receive Slack event

    Returns:
        flask.Response -- Flask HTTP Response
    """
    # Create event controller instance
    controller = EventController()

    # Execute controller process
    response_object = controller.main()

    # Response
    return response_object


if __name__ == '__main__':
    app.run()
