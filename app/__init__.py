from flask import Flask
from .config import Config
from .extensions import db, cors, jwt
from .adapters.api.routes import register_routes
from flask_restful import Api
from app.adapters.api.controllers import ClienteController, SolicitudController, PlanController


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    api = Api(app)
    register_routes(api)
    
    return app
