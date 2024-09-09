from flask_restful import Api
from microservicio_proceso_solicitud.adapters.api.controllers import IntegracionController

def register_routes(api: Api):
    api.add_resource(IntegracionController, '/integraciones/solicitudes')