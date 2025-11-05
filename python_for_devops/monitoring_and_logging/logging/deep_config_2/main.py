from log_config import root_logger, app_logger
import time

root_logger.warning("This is a root warning")

for i in range(5):
    app_logger.info(f"Processing item {i}")
    app_logger.warning(f"Item {i} might fail")
    time.sleep(1)
