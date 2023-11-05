import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import settings

lg = logging.getLogger(__name__)
pcc = Flask(__name__)
pcc.config["SQLALCHEMY_DATABASE_URI"] = settings.CONNECTION_STRING

from utils import datetime_helpers, db_helpers, http, trade
from models import base_models

with pcc.app_context():
    base_models.db.init_app(pcc)
    base_models.db.create_all()
    base_models.db.reflect()
    
    trade.get_companies_list(settings.broker_client)
    # trade.get_ticker_data(settings.broker_client)