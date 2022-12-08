from flask import Flask

from resources.api import api
from service.config import init_config
from service.json_logger import init_json_logger
from service.reporting_service import reporting_service

app = Flask(__name__)

init_json_logger()

init_config(app)
api.init_app(app)
reporting_service.init_app(app)
