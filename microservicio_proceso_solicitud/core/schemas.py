from microservicio_proceso_solicitud.adapters.persistence.models import Integracion
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields


class IntegracionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Integracion
        include_relationships=True
        load_instance = True 


