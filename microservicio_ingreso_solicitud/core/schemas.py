from ..adapters.persistence.models import Cliente, Solicitud, Plan
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from ..enums.enums import Estado, TipoPlan

class EnumToDic(fields.Field):
    def __init__(self, enum_type, *args, **kwargs):
        self.enum_type = enum_type
        super().__init__(*args, **kwargs)

    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {'key': value.name, 'valor': value.value}

    def _deserialize(self, value, attr, data, **kwargs):
        if isinstance(value, dict) and 'key' in value:
            try:
                return self.enum_type[value['key']]
            except KeyError:
                raise ValidationError(f"Invalid value for enum: {value['key']}")
        elif isinstance(value, str):
            try:
                return self.enum_type[value]
            except KeyError:
                raise ValidationError(f"Invalid value for enum: {value}")
        raise ValidationError('Invalid value for enum')


class ClienteSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Cliente
        include_relationships=True
        load_instance = True 
    plan_id = fields.Int()

class SolicitudSchema(SQLAlchemyAutoSchema):
    estado = EnumToDic(enum_type=Estado) 
    class Meta:
        model = Solicitud
        include_relationships=True
        load_instance = True
        exclude = ('fecha_procesamiento',) 
    cliente_id = fields.Int()
    

class PlanSchema(SQLAlchemyAutoSchema):
    tipo_plan = EnumToDic(enum_type=TipoPlan) 
    class Meta:
        model = Plan
        include_relationships=True
        load_instance = True
     

