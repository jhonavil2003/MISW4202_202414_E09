from flask_restful import Resource
from flask import request
from microservicio_proceso_solicitud.core.services import IntegracionService  

class IntegracionController(Resource):
    def get(self):
        return IntegracionService.get_all_solicitudes_queue()