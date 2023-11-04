import os
from dotenv import load_dotenv, find_dotenv

from logger.log import lg

lg.info(f"loaded env variables: {load_dotenv(find_dotenv())}")

API_KEY = os.getenv('API_KEY')

# Database configs
DB_ENV_PROD = int(os.getenv('DB_ENV_PROD'))

if DB_ENV_PROD:
	CONNECTION_STRING = os.getenv('CLOUD_DB_CONNECTION_STRING')
else:
	CONNECTION_STRING = os.getenv('LOCAL_DB_CONNECTION_STRING')

REMOTE_HOST 	= os.environ.get('REMOTE_HOST')
REMOTE_USERNAME = os.environ.get('REMOTE_USERNAME')
PKEY_PATH		= os.environ.get('PRIVATE_KEY_PATH')
