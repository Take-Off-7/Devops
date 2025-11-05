import logging
from logging.config import dictConfig


LOG_CONFIG = {
    'version': 1,
    'formatters': {
        'BASE_FORMAT': {
            'format': '[%(name)s][%(levelname)-6s] %(message)s',
        },
        'FILE_FORMAT': {
            'format': '[%(asctime)s] [%(name)s][%(levelname)-6s] %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'WARNING',
            'formatter': 'BASE_FORMAT',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'application.log',
            'level': 'DEBUG',
            'formatter': 'FILE_FORMAT',
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'file'],
    },
    'loggers': {
        'my-app': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': False,
        },
    },
}

# Apply configuration
dictConfig(LOG_CONFIG)

# Create loggers
root_logger = logging.getLogger()
app_logger = logging.getLogger('my-app')
