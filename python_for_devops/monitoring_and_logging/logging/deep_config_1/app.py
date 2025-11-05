from log_test import root_logger, app_logger
import time

for i in range(5):
    app_logger.info(f"Processing item {i}")       # goes to file only
    app_logger.warning(f"Item {i} might fail")   # goes to file + console
    time.sleep(1)
