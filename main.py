import logging

from settings import *
from src.utils.datetime_helpers import get_day

lg = logging.getLogger(__name__)
lg.info(get_day())
