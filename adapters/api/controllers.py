from flask_restful import Resource
from flask import request
from core.services import  PermisosService, UserService, RoleService ,UserRolesService

class UserController(Resource):
 
     def get(self, user_id=None):
        if user_id:
  
            user = UserService.get_user_by_id(user_id)
            if user:
                return user
            return {'message': 'User not found'}, 404
        else:
          
            users = UserService.get_all_users()
            return users
 
    

class RolesController(Resource):
    
    def get(self , role_id=None):
        if role_id:
            role = RoleService.get_role_by_id(role_id)
            if role:
                return role
            return {'message': 'Role not found'}, 404
        else:
            roles = RoleService.get_all_roles()
            return roles
        


class PermisosController(Resource):
    def get(self , permiso_id=None):
        if permiso_id:
            permiso = PermisosService.get_permiso_by_id(permiso_id)
            if permiso:
                return permiso
            return {'message': 'Permiso not found'}, 404
        else:
            permisos = PermisosService.get_all_permisos()
            return permisos


class GestorController(Resource):
    def get(self, user_id=None):
            if user_id:
    
                user = UserService.get_user_by_id(user_id)
                if user:
                    return user
                return {'message': 'User not found'}, 404
            else:
            
                users = UserService.get_all_users()
                return users
    

    
class UserRolesController(Resource):
    def get(self , user_role_id=None):
        if user_role_id:
            user_role = UserRolesService.get_user_role_by_id(user_role_id)
            if user_role:
                return user_role
            return {'message': 'User Role not found'}, 404
        else:
            user_roles = UserRolesService.get_all_user_roles()
            return user_roles
    


    
    
    
