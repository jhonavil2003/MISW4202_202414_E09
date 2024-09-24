from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from adapters.persistence.models import  Users

    
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        include_relationships = True
        load_instance = True
    
