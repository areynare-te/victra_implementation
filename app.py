from flask import Flask, jsonify
import os
import sys
from src.blueprints.manager_app import application, manager_app

# Start manager app
# manager_app.init_manager_app()

# Start application
if __name__ == '__main__':
    application.run(debug=True)
    