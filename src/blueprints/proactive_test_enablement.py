from flask import Flask, jsonify, request, Blueprint
import requests, logging

# Import commands
from src.commands.enable_tests import enable_test
from src.commands.disable_tests import disable_test

# Define blueprint
proactive_test_enablement = Blueprint('proactive_test_enablement', __name__)

# Configuración de registro
logging.basicConfig(filename='flask_app.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Routes and functions
@proactive_test_enablement.route('/alert', methods = ['POST'])
def receive_alert():
    try:
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
            if token == "TestToken4":
                alert_body = request.json
                test_name = alert_body['alert']['rule']['name']
                if alert_body['type'] == "2":
                    enable_test(test_name)
                    logger.info("Enabled Test: %s", test_name)
                else:
                    disable_test(test_name)
                    logger.info("Disabled Test: %s", test_name)
                return "Received Alert", 200
            else:
                logger.warning("Unauthorized request")
                return "Unauthorized", 403
        else:
            logger.warning("Unauthorized request")
            return "Unauthorized", 403
    except Exception as e:
        logger.error("Error processing alert: %s", str(e))
        return "Internal Server Error", 500
    
@proactive_test_enablement.route('/ping', methods = ['GET'])
def heatlh_check():
    return "pong", 200
