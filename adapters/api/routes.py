from flask_restful import Api
from adapters.api.controllers import PermisosController, UserController ,RolesController, UserRolesController

def register_routes(api: Api):
    api.add_resource(UserController, '/users')
    api.add_resource(RolesController, '/roles')
    api.add_resource(PermisosController, '/permisos')
    api.add_resource(UserRolesController, '/user_roles')