# logging_demo.py
import os
from log_setup import app_logger

# Optional: set the environment variable dynamically
# (in real apps, this might come from deployment configuration)
os.environ['APP_ENVIRON'] = 'PRODUCTION'

# Log some sample messages
app_logger.info("Starting application...")
app_logger.warning("This is a warning in production mode!")
app_logger.error("Something went wrong!")

# Simulate a different environment
os.environ['APP_ENVIRON'] = 'STAGING'
app_logger.info("Running in staging now...")
