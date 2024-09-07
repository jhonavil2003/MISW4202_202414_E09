from flask_restful import Resource
from flask import request
from ...core.services import ClienteService, SolicitudService, PlanService

class ClienteController(Resource):
    def get(self):
        return ClienteService.get_all_clients()

    def post(self):
        data = request.get_json()
        return ClienteService.create_client(data)

class SolicitudController(Resource):
    def get(self):
        return SolicitudService.get_all_requests()

    def post(self):
        data = request.get_json()
        return SolicitudService.create_request(data)

class PlanController(Resource):
    def get(self):
        return PlanService.get_all_plans()

    def post(self):
        data = request.get_json()
        return PlanService.create_plan(data)
