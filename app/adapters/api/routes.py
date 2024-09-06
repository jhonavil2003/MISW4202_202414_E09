from flask_restful import Api
from app.adapters.api.controllers import ClienteController, SolicitudController, PlanController

def register_routes(api: Api):
    api.add_resource(ClienteController, '/clientes')
    api.add_resource(SolicitudController, '/solicitudes')
    api.add_resource(PlanController, '/planes')