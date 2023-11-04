import os
from dotenv import load_dotenv, find_dotenv

from logger.log import lg

lg.info(f"loaded env variables: {load_dotenv(find_dotenv())}")

API_KEY = os.environ.get('API_KEY')

# Database configs
DB_ENV_PROD = int(os.environ.get('DB_ENV_PROD'))

if DB_ENV_PROD == 1:
	conn_params = {
		'database'	: os.environ.get('CLOUD_DB_NAME'), 
		'user'		: os.environ.get('CLOUD_DB_USER'), 
		'password'	: os.environ.get('CLOUD_DB_PASSWORD'), 
		'host'		: os.environ.get('DB_HOST'), 
		'port'		: int(os.environ.get('DB_PORT'))
		}
else:
	conn_params = {
		'database'	: os.environ.get('LOCAL_DB_NAME'), 
		'user'		: os.environ.get('LOCAL_DB_USER'), 
		'password'	: os.environ.get('LOCAL_DB_PASSWORD'), 
		'host'		: os.environ.get('DB_HOST'), 
		'port'		: int(os.environ.get('DB_PORT'))
		}

REMOTE_HOST 	= os.environ.get('REMOTE_HOST')
REMOTE_USERNAME = os.environ.get('REMOTE_USERNAME')
PKEY_PATH		= '~/.ssh/stock-mkt-key.pem'
