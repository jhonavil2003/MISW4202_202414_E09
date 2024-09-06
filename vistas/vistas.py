from flask import jsonify, request
from flask_restful import Resource
from modelos.modelos import Plan, db,Cliente, Solicitud
from schemas.schemas import ClienteSchema, SolicitudSchema, PlanSchema

cliente_schema = ClienteSchema()
solicitud_schema = SolicitudSchema()
plan_schema = PlanSchema()

class VistaCliente(Resource):
    def get(self):
        return [cliente_schema.dump(cliente) for cliente in Cliente.query.all()]
    
    def post(self):
        data = request.json
        cliente = cliente_schema.load(data, session=db.session)
        db.session.add(cliente)
        db.session.commit()
        return cliente_schema.dump(cliente), 201
     
class VistaSolicitud(Resource):
    def get(self):
        return [solicitud_schema.dump(solicitud) for solicitud in Solicitud.query.all()]
    
    def post(self):
        data = request.json
        solicitud = solicitud_schema.load(data, session=db.session)
        db.session.add(solicitud)
        db.session.commit()
        return solicitud_schema.dump(solicitud), 201

class VistaPlan(Resource):
    def get(self):
        return [plan_schema.dump(plan) for plan in Plan.query.all()]
    
    def post(self):
        data = request.json
        plan = plan_schema.load(data, session=db.session)
        db.session.add(plan)
        db.session.commit()
        return plan_schema.dump(plan), 201