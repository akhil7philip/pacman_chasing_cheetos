import os
import logging
from urllib.parse import urlparse
# from sshtunnel import SSHTunnelForwarder
import mysql.connector
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

import settings

lg = logging.getLogger(__name__)

url = urlparse(settings.CONNECTION_STRING)
pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="pcc_db_pool",
    pool_size=15,
    pool_reset_session=True,
    host=url.hostname,
    port=url.port,
    user=url.username,
    password=url.password,
    database=url.path.strip('/')
)

def conn_db(func):
    from functools import wraps
    @wraps(func)
    def wrapper(*args, **kwargs):
        if settings.DB_ENV_PROD:
            lg.info('connecting to production database')
            # tunnel = SSHTunnelForwarder((REMOTE_HOST),
            #     ssh_pkey=PKEY_PATH,
            #     ssh_username=REMOTE_USERNAME,
            #     remote_bind_address=(conn_params['host'],int(conn_params['port'])),
            #     )
            # tunnel.start()
            # conn_params['port'] = tunnel.local_bind_port
        else: 
            lg.info('connecting to local database')
        
        conn = pool.get_connection()
        try:
            cursor = conn.cursor()
            result = func(cursor=cursor, *args, **kwargs)
            cursor.close()
        finally:
            conn.close()
            lg.info('closed connection')
            # if settings.DB_ENV_PROD: 
            #     tunnel.stop()
        return result
    return wrapper

@conn_db
def run_query(query, cursor, params=None):
    cursor.execute(query, params)
    result = cursor.fetchall()
    return result

@conn_db
def commit_query(query, cursor, params=None):
    cursor.execute(query, params)
    cursor.execute("commit")


def save_values(values, db, model):
    failed = 0
    for row in values:
        try:
            db.session.add(model(**row))
            db.session.commit()    
        except Exception as e:
            failed += 1
            lg.error(f"row: {row}; error: {e}")
    lg.info(f'added {len(values)-failed} of total {len(values)} rows to {model.__name__}')
