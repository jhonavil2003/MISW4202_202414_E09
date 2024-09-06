from marshmallow import ValidationError, fields
from enums.enums import Estado, TipoPlan

class EnumToEstado(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {'key': value.name, 'valor': value.value}
    
    def _deserialize(self, value, attr, data, **kwargs):
        if isinstance(value, dict) and 'key' in value:
            try:
                return Estado[value['key']]
            except KeyError:
                raise ValidationError(f"Invalid Estado value: {value['key']}")
        elif isinstance(value, str):
            try:
                return Estado[value]
            except KeyError:
                raise ValidationError(f"Invalid Estado value: {value}")
        raise ValidationError('Invalid value for enum')
    
    
class EnumToDicPlan(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {'key': value.name, 'valor': value.value}
    
    def _deserialize(self, value, attr, data, **kwargs):
        if isinstance(value, dict) and 'key' in value:
            try:
                return TipoPlan[value['key']]
            except KeyError:
                raise ValidationError(f"Invalid TipoPlan value: {value['key']}")
        elif isinstance(value, str):
            try:
                return TipoPlan[value]
            except KeyError:
                raise ValidationError(f"Invalid TipoPlan value: {value}")
        raise ValidationError('Invalid value for enum')