# logging_config.py
import os
import logging
from logging.config import dictConfig

# Define a custom filter that injects environment info into each log record
class EnvironFilter(logging.Filter):
    def filter(self, record):
        record.app_environment = os.environ.get('APP_ENVIRON', 'DEVEL')
        return True

# Centralized logging configuration
dictConfig({
    'version': 1,
    'filters': {
        'environ_filter': {
            '()': EnvironFilter  # Instantiate the custom filter
        }
    },
    'formatters': {
        'BASE_FORMAT': {
            'format': '[%(app_environment)s][%(name)s][%(levelname)-6s] %(message)s',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'BASE_FORMAT',
            'filters': ['environ_filter'],  # Attach the custom filter
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console']
    }
})

# Create a named logger (optional but recommended)
app_logger = logging.getLogger('my-app')
