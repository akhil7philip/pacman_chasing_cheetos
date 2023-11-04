import logging
import datetime as dt

lg = logging.getLogger(__name__)

def get_day():
    day = str(dt.datetime.now().day), str(dt.datetime.now().month)
    lg.info(day)
    return day

today = dt.datetime.today().date()