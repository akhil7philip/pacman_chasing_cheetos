import os
from dotenv import load_dotenv, find_dotenv
from pya3 import *

from logger.log import lg

lg.info(f"loaded env variables: {load_dotenv(find_dotenv())}")

FMCLOUD_API_KEY = os.getenv('FMCLOUD_API_KEY')

broker_client = Aliceblue(
	user_id=str(os.environ.get('ALICE_BLUE_USERNAME')),
	api_key=os.environ.get('ALICE_BLUE_API_KEY'))
broker_client.get_session_id() # Get Session ID

# Database configs
DB_ENV_PROD = int(os.getenv('DB_ENV_PROD'))

if DB_ENV_PROD:
	CONNECTION_STRING = os.getenv('CLOUD_DB_CONNECTION_STRING')
else:
	CONNECTION_STRING = os.getenv('LOCAL_DB_CONNECTION_STRING')

REMOTE_HOST 	= os.environ.get('REMOTE_HOST')
REMOTE_USERNAME = os.environ.get('REMOTE_USERNAME')
PKEY_PATH		= os.environ.get('PRIVATE_KEY_PATH')
