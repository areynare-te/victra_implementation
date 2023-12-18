from flask import Flask, jsonify, request, Blueprint
import requests

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
            print(alert_name + '\n')
            if "details" in alert_body.get("alert", {}):
                details = alert_body["alert"]["details"]
                for detail in details:
                    source_id = detail.get("source", {}).get("name")
                    print(source_id+ '\n')
                # Send PUT request
                enable_body = {"enabled": 'true'}
                headers = {"Authorization": "Bearer 05dd35b2-863a-469c-86da-99e74ba499d8"}
                enable_response = requests.put("https://api.thousandeyes.com/v7/tests/http-server/4519688?aid=1129196", json=enable_body, headers=headers)
            return "Received Alert", 200
        else:
            return "Unauthorized", 403
    else:
        return "Unauthorized", 403

@proactive_test_enablement.route('/ping', methods = ['GET'])
def heatlh_check():
    return "pong", 200
