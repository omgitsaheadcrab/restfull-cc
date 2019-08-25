import os

def gen_connection_string():
    # if not on Google then use local MySQL
    if not os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        return 'mysql://root@localhost/restfulcc'
    else:
        conn_name = os.environ.get('CLOUDSQL_CONNECTION_NAME' '')
        sql_user = os.environ.get('CLOUDSQL_USER', 'root')
        sql_pass = os.environ.get('CLOUDSQL_PASSWORD', '')
        conn_template = 'mysql+mysqldb://%s:%s@/restfulcc?unix_socket=/cloudsql/%s'
        return conn_template % (sql_user, sql_pass, conn_name)
