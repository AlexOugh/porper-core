
region = 'us-east-1'
from connection import connection

from user_role import UserRole
#user_role = UserRole(connection)
user_role = UserRole(region)

user_role.find({'user_id':'b2fc88a6-7253-4850-8d5a-07639b1315aa'})
user_role.find({'role_id':'3867c370-552f-43b8-bed9-6aa00ffc41b4'})
user_role.find({'user_id':'c8b5dbbe-edd1-4e78-b03a-63b0d779be85', 'role_id':'435a6417-6c1f-4d7c-87dd-e8f6c0effc7a'})

user_role.create({'user_id':'b2fc88a6-7253-4850-8d5a-07639b1315aa', 'role_id':'ffffffff-ffff-ffff-ffff-ffffffffffff', 'is_admin':False})
user_role.create({'user_id':'49d8bc68-f57e-11e3-ba1d-005056ba0d15', 'role_id':'3867c370-552f-43b8-bed9-6aa00ffc41b4', 'is_admin':False})
user_role.create({'user_id':'49d8bc68-f57e-11e3-ba1d-005056ba0d15', 'role_id':'435a6417-6c1f-4d7c-87dd-e8f6c0effc7a', 'is_admin':False})
user_role.create({'user_id':'c8b5dbbe-edd1-4e78-b03a-63b0d779be85', 'role_id':'435a6417-6c1f-4d7c-87dd-e8f6c0effc7a', 'is_admin':False})
user_role.create({'user_id':'c8b5dbbe-edd1-4e78-b03a-63b0d779be85', 'role_id':'3867c370-552f-43b8-bed9-6aa00ffc41b4', 'is_admin':False})
user_role.create({'user_id':'117043220775623860708', 'role_id':'435a6417-6c1f-4d7c-87dd-e8f6c0effc7a', 'is_admin':False})
user_role.create({'user_id':'117043220775623860708', 'role_id':'3867c370-552f-43b8-bed9-6aa00ffc41b4', 'is_admin':True})
