from flask import Flask, jsonify, request, Blueprint
import requests

from src.commands.enable_tests import enable_test
from src.commands.disable_tests import disable_test

# Define blueprint
proactive_test_enablement = Blueprint('proactive_test_enablement', __name__)


# Routes and functions
@proactive_test_enablement.route('/alert', methods = ['POST'])
def receive_alert():
    if "Authorization" in request.headers:
        token = request.headers["Authorization"].split(" ")[1]
        if token == "TestToken4":
            alert_body = request.json
            test_name = alert_body['alert']['rule']['name']
            if alert_body['type']['id'] == "2":
                enable_test(test_name)
            else:
                disable_test(test_name)
            return "Received Alert", 200
        else:
            return "Unauthorized", 403
    else:
        return "Unauthorized", 403

@proactive_test_enablement.route('/ping', methods = ['GET'])
def heatlh_check():
    return "pong", 200
