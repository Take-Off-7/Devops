import logging
import os


BASE_FORMAT = "[%(name)s][%(levelname)-6s] %(message)s"
FILE_FORMAT = "[%(asctime)s]" + BASE_FORMAT

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

try:
    file_logger = logging.FileHandler('application.log')
except (OSError, IOError):
    file_logger = logging.FileHandler('/tmp/application.log')
    
    
file_logger.setLevel(logging.INFO)
file_logger.setFormatter(logging.Formatter(BASE_FORMAT))
root_logger.addHandler(file_logger)

console_logger = logging.StreamHandler()
console_logger.setFormatter(logging.Formatter(BASE_FORMAT))
console_logger.setLevel(logging.WARNING)
root_logger.addHandler(console_logger)

logger = logging.getLogger()
logger.warning('this is an info message from the root logger')
    
app_logger = logging.getLogger('my-app')
app_logger.warning('an info message from my-app')
