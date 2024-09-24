from flask_restful import Api
from adapters.api.controllers import PermisosController, UserController ,RolesController, UserRolesController

def register_routes(api: Api):
    api.add_resource(UserController, '/users', '/users/<int:user_id>')
    api.add_resource(RolesController, '/roles','/roles/<int:role_id>')
    api.add_resource(PermisosController, '/permisos','/permisos/<int:permiso_id>')
    api.add_resource(UserRolesController, '/user_roles','/user_roles/<int:user_role_id>')