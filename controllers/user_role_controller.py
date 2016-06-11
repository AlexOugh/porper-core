
import sys
sys.path.insert(0, r'..')

ADMIN_ROLE_ID = 'ffffffff-ffff-ffff-ffff-ffffffffffff'

class UserRoleController:

    def __init__(self, connection):
        self.connection = connection
        from models.user import User
        from models.role import Role
        from models.user_role import UserRole
        self.user = User(connection)
        self.role = Role(connection)
        self.user_role = UserRole(connection)

    def find_by_user_id(self, user_id):
        user_roles = self.user_role.find({'user_id': user_id})
        print user_roles
        ids = [ user_role['role_id'] for user_role in user_roles ]
        if ADMIN_ROLE_ID in ids:
            params = {}
        else:
            ids = [ user_role['role_id'] for user_role in user_roles if user_role['is_admin'] ]
            params = {'ids': ids}
        print params
        return self.role.find(params)

    def find_by_role_id(self, role_id):
        user_roles = self.user_role.find({'role_id': role_id})
        print user_roles
        ids = [row['user_id'] for row in user_roles]
        params = {'ids': ids}
        print params
        return self.user.find(params)
