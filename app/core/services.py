from app.adapters.persistence.models import Cliente, Solicitud, Plan
from app.core.schemas import ClienteSchema, SolicitudSchema, PlanSchema
from ..extensions import db, cors, jwt

cliente_schema = ClienteSchema()
solicitud_schema=SolicitudSchema()
plan_schema=PlanSchema()


class ClienteService:
    @staticmethod
    def get_all_clients():
        return [cliente_schema.dump(cliente) for cliente in Cliente.query.all()]
        
    @staticmethod
    def create_client(data):
        cliente = cliente_schema.load(data, session=db.session)
        db.session.add(cliente)
        db.session.commit()
        return cliente_schema.dump(cliente), 201

class SolicitudService:
    @staticmethod
    def get_all_requests():
        return [solicitud_schema.dump(solicitud) for solicitud in Solicitud.query.all()]

    @staticmethod
    def create_request(data):
        solicitud = solicitud_schema.load(data, session=db.session)
        db.session.add(solicitud)
        db.session.commit()
        return solicitud_schema.dump(solicitud), 201

class PlanService:
    @staticmethod
    def get_all_plans():
        return [plan_schema.dump(plan) for plan in Plan.query.all()]

    @staticmethod
    def create_plan(data):
        plan = plan_schema.load(data, session=db.session)
        db.session.add(plan)
        db.session.commit()
        return plan_schema.dump(plan), 201
