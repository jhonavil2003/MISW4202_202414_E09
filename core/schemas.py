from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from adapters.persistence.models import  Roles, Users

    
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        include_relationships = True
        load_instance = True

class RoleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Roles
        include_relationships = True
        load_instance = True

class PermisoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Roles
        include_relationships = True
        load_instance = True
    
