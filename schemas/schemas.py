
from dictionary.dictionary import EnumToDicPlan, EnumToEstado
from modelos import Cliente, Solicitud, Plan
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields



class ClienteSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Cliente
        include_relationships=True
        load_instance = True 
    plan_id = fields.Int()

class SolicitudSchema(SQLAlchemyAutoSchema):
    estado = EnumToEstado(attribute="estado") 
    class Meta:
        model = Solicitud
        include_relationships=True
        load_instance = True
    cliente_id = fields.Int()
    

class PlanSchema(SQLAlchemyAutoSchema):
    tipo_plan = EnumToDicPlan(attribute="tipo_plan") 
    class Meta:
        model = Plan
        include_relationships=True
        load_instance = True
     

