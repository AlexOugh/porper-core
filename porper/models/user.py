
class User:

    def __init__(self, connection):
        self.connection = connection

    def create(self, params):
        sql = "INSERT INTO users (id, email, family_name, given_name, name) VALUES ('" + params['id'] + "', '" + params['email'] + "', '" + params['family_name'] + "', '" + params['given_name'] + "', '" + params['given_name'] + " " + params['family_name'] + "')"
        print sql
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
        return params['id']

    def find(self, params):
        if params.get('ids') == [] or params.get('role_ids') == []:
            return []
        if params.get('role_id') or params.get('role_ids'):
            sql = "SELECT u.*, ur.is_admin FROM users u JOIN users_roles ur ON u.id = ur.user_id"
            if params.get('role_id'):
                sql += " WHERE u.id IN (SELECT user_id FROM users_roles WHERE role_id = '" + params['role_id'] + "')"
            elif params.get('role_ids'):
                sql += " WHERE u.id IN (SELECT user_id FROM users_roles WHERE role_id IN ('" + "','".join(params['role_ids']) + "'))"
            print sql
            rows = []
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                for row in cursor:
                    rows.append({'id':row[0], 'email':row[1], 'family_name':row[2], 'given_name':row[3], 'name':row[4], 'is_admin':row[5]})
            return rows
        else:
            sql = "SELECT * FROM users"
            if params.get('email'):
                sql += " WHERE email = '" + params['email'] + "'"
            elif params.get('ids'):
                sql += " WHERE id IN ('" + "','".join(params['ids']) + "')"
            elif params.get('id'):
                sql += " WHERE id = '" + params['id'] + "'"
            print sql
            rows = []
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                for row in cursor:
                    rows.append({'id':row[0], 'email':row[1], 'family_name':row[2], 'given_name':row[3], 'name':row[4]})
            return rows
