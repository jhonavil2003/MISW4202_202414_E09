from flask_restful import Resource
from flask import request
from core.services import  PermisosService, UserService, RoleService ,UserRolesService

class UserController(Resource):
    def get(self):
        return UserService.get_all_users()
    

class RolesController(Resource):
    def get(self):
        return RoleService.get_all_roles()

class PermisosController(Resource):
    def get(self):
        return PermisosService.get_all_permisos()
    
class UserRolesController(Resource):
    def get(self):
        return UserRolesService.get_all_user_roles()
    


    
    
    
