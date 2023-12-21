from flask import Flask
import logging
from src.blueprints.proactive_test_enablement import proactive_test_enablement

# Configure application
application = Flask(__name__)
application.register_blueprint(proactive_test_enablement)
application.logger.addHandler(logging.FileHandler('flask_app.log'))
application.logger.setLevel(logging.INFO)
application.run(debug=True)

# Create manager app
class ManagerApp():
    def __init__(self, app) -> None:
        self.app = app

# Start app
manager_app = ManagerApp(application)