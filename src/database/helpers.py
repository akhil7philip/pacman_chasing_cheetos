import logging


def get_sqlalchemy_engine(db, host, user, password, database, port):
    print(f"db, host, user, password, database, port: {db, host, user, password, database, port}")
    if db == 'mysql':
        return create_engine("mysql+pymysql://{user}:{password}@{host}:{port}/{database}".format(**conn_params[db]))
    else:
        return create_engine("postgresql://{user}:{password}@{host}:{port}/{database}".format(**conn_params[db]))

# @open_ssh_tunnel
def run_query(query, db='mysql'):
    logger.info('connecting...')
    curr = get_cursor(db, **conn_params[db])
    logger.info('connected')
    curr.execute(query)
    result = curr.fetchall()
    curr.close()
    return result