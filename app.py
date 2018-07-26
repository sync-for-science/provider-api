import os

from flask import Flask
from flask_cors import CORS

from views import BP


APP = Flask(__name__)
APP.register_blueprint(BP)


APP.config["APP_ID"] = os.environ.get("APP_ID", "provider-api")
APP.config["FHIR_BASE"] = os.environ.get("FHIR_BASE", "http://localhost:8080/baseDstu3")


CORS().init_app(APP)
