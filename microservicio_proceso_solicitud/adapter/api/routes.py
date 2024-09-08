from flask_restful import Api
from microservicio_proceso_solicitud.adapter.api.controllers import SolicitudController

def register_routes(api: Api):
    api.add_resource(SolicitudController, '/integraciones/solicitudes')