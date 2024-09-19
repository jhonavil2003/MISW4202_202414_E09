from flask_restful import Resource
from flask import request
from core.services import AuthService, LogService

class LogController(Resource):
    def get(self):
        return LogService.get_all_logs()
    
class AuthController(Resource):
    def post(self):
        data = request.get_json()
        return AuthService.validate_auth(data)