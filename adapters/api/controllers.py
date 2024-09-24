from flask_restful import Resource
from flask import request
from core.services import AuthService, UserService

class LogController(Resource):
    def get(self):
        return UserService.get_all_users()
    
    
    
