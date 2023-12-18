from flask import Flask, jsonify, request, Blueprint

# Define blueprint
proactive_test_enablement = Blueprint('proactive_test_enablement', __name__)


# Routes and functions
@proactive_test_enablement.route('/alert', methods = ['POST'])
def receive_alert():
    if "Authorization" in request.headers:
        token = request.headers["Authorization"].split(" ")[1]
        if token == "TestToken4":
            alert_body = request.json
            alert_name = alert_body["alert"]["rule"]["name"]
            print(alert_name)
            return "Received Alert", 200
        else:
            return "Unauthorized", 403
    else:
        return "Unauthorized", 403

@proactive_test_enablement.route('/ping', methods = ['GET'])
def heatlh_check():
    return "pong", 200
