from core.schemas import LogSchema
from extensions import db
from adapters.persistence.models import Users

clienteSchema = LogSchema()

class LogService:
    @staticmethod
    def get_all_logs():
        return [clienteSchema.dump(cliente) for cliente in Users.query.all()]
    
    @staticmethod
    def create_log():
        pass
    
class AuthService:    
    @staticmethod
    def validate_auth(data):
        pass