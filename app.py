from flask import Flask
from flask_cors import CORS
from views import BP


APP = Flask(__name__)
APP.register_blueprint(BP)

CORS().init_app(APP)
