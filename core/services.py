from core.schemas import UserSchema
from extensions import db
from adapters.persistence.models import Users

user_schema = UserSchema()

class UserService:
    @staticmethod
    def get_all_users():
        return [user_schema.dump(user) for user in Users.query.all()]
    
    @staticmethod
    def create_log():
        pass
    
class AuthService:    
    @staticmethod
    def validate_auth(data):
        pass