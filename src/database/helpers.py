import os
import logging
from sqlalchemy import create_engine

lg = logging.getLogger(__name__)



conn_mysql = create_engine(os.getenv(''))

def get_cursor(db, host, user, password, database, port):
    print(f"db, host, user, password, database, port: {db, host, user, password, database, port}")
    if db == 'mysql':
        conn = mysql.connect(host=host, user=user, passwd=password, database=database, port=port)
        return conn.cursor(dictionary=True)
    else:
        conn = psycopg2.connect(host=host, user=user, password=password, database=database, port=port)    
        return conn.cursor()
    
# @open_ssh_tunnel
def run_query(query, db='mysql'):
    lg.info('connecting...')
    curr = get_cursor(db, **conn_params[db])
    lg.info('connected')
    curr.execute(query)
    result = curr.fetchall()
    curr.close()
    return result