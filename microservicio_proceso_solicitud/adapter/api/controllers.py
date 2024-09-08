from flask_restful import Resource
from flask import request
from microservicio_proceso_solicitud.core.services import SolicitudService  

class SolicitudController(Resource):
    def get(self):
        return SolicitudService.get_all_solicitudes_queue()