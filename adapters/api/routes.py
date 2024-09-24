from flask_restful import Api
from adapters.api.controllers import LogController

def register_routes(api: Api):
    api.add_resource(LogController, '/log')