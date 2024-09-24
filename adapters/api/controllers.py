from flask_restful import Resource
from flask import request
from core.services import AuthService, LogService

class LogController(Resource):
    def get(self):
        return LogService.get_all_logs()
    
