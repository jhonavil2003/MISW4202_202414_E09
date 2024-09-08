from flask import Flask
from microservicio_proceso_solicitud.config import Config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Config)
    return app