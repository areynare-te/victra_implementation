from flask import Flask, jsonify, request, Blueprint

# Define blueprint
proactive_test_enablement = Blueprint('proactive_test_enablement', __name__)

@proactive_test_enablement.route('/ping', methods = ['GET'])
def heatlh_check():
    return "pong", 200
