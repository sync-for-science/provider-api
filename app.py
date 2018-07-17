from flask import Flask
from views import BP


APP = Flask(__name__)
APP.register_blueprint(BP)
