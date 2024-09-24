from core.schemas import UserSchema,RoleSchema,PermisoSchema
from extensions import db
from adapters.persistence.models import Permisos, Roles, UserRoles, Users

user_schema = UserSchema()
role_schema = RoleSchema()
permiso_schema = PermisoSchema()

class UserService:
    @staticmethod
    def get_all_users():
        return [user_schema.dump(user) for user in Users.query.all()]
    
    def get_user_by_id(user_id):
        return user_schema.dump(Users.query.get(user_id))
    
    
    
class RoleService:    
    @staticmethod
    def get_all_roles():
        return [role_schema.dump(role) for role in Roles.query.all()]
    
    def get_role_by_id(role_id):
        return role_schema.dump(Roles.query.get(role_id))
    

class  PermisosService:
    @staticmethod
    def get_all_permisos():
        return [permiso_schema.dump(permiso) for permiso in Permisos.query.all()]
    
    def get_permiso_by_id(permiso_id):
        return permiso_schema.dump(Permisos.query.get(permiso_id))
    
    

class UserRolesService:
    @staticmethod
    def get_all_user_roles():
        user_roles = db.session.query(UserRoles).join(Users, UserRoles.user_id == Users.id).join(Roles, UserRoles.role_id == Roles.id).add_columns(
            Users.username.label('user_name'), Roles.nombre.label('role_name') , Roles.id.label('role_id')).all()
        return [{'user_name': user_role.user_name, 'role_name': user_role.role_name , 'role_id':user_role.role_id } for user_role in user_roles]
    
    def get_user_role_by_id(user_role_id):
        user_role = db.session.query(UserRoles).join(Users, UserRoles.user_id == Users.id).join(Roles, UserRoles.role_id == Roles.id).add_columns(
            Users.username.label('user_name'), Roles.nombre.label('role_name') , Roles.id.label('role_id')).filter(UserRoles.user_id == user_role_id).first()
        return {'user_name': user_role.user_name, 'role_name': user_role.role_name , 'role_id':user_role.role_id }




