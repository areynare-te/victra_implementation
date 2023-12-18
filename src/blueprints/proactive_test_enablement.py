from flask import Flask, jsonify, request, Blueprint

# Define blueprint
proactive_test_enablement = Blueprint('proactive_test_enablement', __name__)


# Routes and functions
@proactive_test_enablement.route('/alert', methods = ['POST'])
def receive_alert():
    if "Authorization" in request.headers:
        token = request.headers("Authorization").split(" ")[1]
        return token, 200
    else:
        return "Unauthorized", 403

@proactive_test_enablement.route('/ping', methods = ['GET'])
def heatlh_check():
    return "pong", 200
