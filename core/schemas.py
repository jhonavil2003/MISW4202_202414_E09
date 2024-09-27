from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from adapters.persistence.models import Roles, Users

class RoleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Roles
        include_relationships = True
        load_instance = True

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        include_relationships = True
        load_instance = True
        ordered = True

    roles = fields.Method("get_roles")

    def get_roles(self, obj):
        return [{"nombre": role.nombre, "tipo": role.tipo} for role in obj.roles]

class PermisoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Roles
        include_relationships = True
        load_instance = True