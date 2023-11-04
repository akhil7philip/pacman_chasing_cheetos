import os
from pathlib import Path

from src.utils import datetime_helpers

base_path = Path(__file__).resolve().parent
log_base_path = f'{base_path}/logs/{datetime_helpers.today}'

if not os.path.isdir(log_base_path):
	os.mkdir(log_base_path)

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'simple': {
			'format': '[%(asctime)s] %(levelname)s %(message)s',
		},
		'verbose': {
			'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
		},
	},
	'handlers': {
		'console': {
			'class': 'logging.StreamHandler',
			'level': 'INFO',
			'formatter': 'verbose'
		},
        'file': {
            'class': 'logging.FileHandler',
            'filename': f'{log_base_path}/stream.log',
            'level': 'INFO',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
			'level': 'INFO',
			'propagate': True,
		},
	},
}
import logging
import logging.config

logging.config.dictConfig(LOGGING)

lg = logging.getLogger(__name__)