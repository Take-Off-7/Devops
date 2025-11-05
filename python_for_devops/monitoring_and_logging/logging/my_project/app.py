# app.py
import logging
import logging.config
from logging.handlers import RotatingFileHandler
from pythonjsonlogger import jsonlogger
from flask import Flask, jsonify, request
from statsd import StatsClient
import time
import traceback

# ---------------------------
# Configuration
# ---------------------------
LOGFILE = "app.log"
LOG_MAX_BYTES = 5 * 1024 * 1024
LOG_BACKUP_COUNT = 3
STATSD_HOST = "127.0.0.1"
STATSD_PORT = 8125
STATSD_PREFIX = "myapp"  # metrics will be like myapp.exceptions

# ---------------------------
# Logging config (dictConfig style)
# ---------------------------
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "plain": {
            "format": "%(asctime)s %(levelname)s %(name)s %(message)s"
        },
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "fmt": "%(asctime)s %(levelname)s %(name)s %(message)s %(pathname)s %(lineno)d"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "plain",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "json",
            "filename": LOGFILE,
            "maxBytes": LOG_MAX_BYTES,
            "backupCount": LOG_BACKUP_COUNT,
            "encoding": "utf8"
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console", "file"]
    },
    "loggers": {
        "werkzeug": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

# ---------------------------
# StatsD client
# ---------------------------
statsd = StatsClient(host=STATSD_HOST, port=STATSD_PORT, prefix=STATSD_PREFIX)

# ---------------------------
# Flask app
# ---------------------------
app = Flask(__name__)

@app.before_request
def before_request():
    # Example: log at debug for each request
    logger.debug("Incoming request: method=%s path=%s remote=%s", request.method, request.path, request.remote_addr)

@app.route("/")
def index():
    logger.info("Index page visited")
    return jsonify({"message": "Hello — try /boom to raise an exception"}), 200

@app.route("/info")
def info_route():
    logger.info("Info endpoint hit")
    return jsonify({"status": "ok", "time": time.time()}), 200

@app.route("/boom")
def boom():
    logger.warning("About to intentionally raise an exception at /boom")
    # This will cause an exception that our error handler will catch
    raise RuntimeError("Intentional failure for testing metrics/logging")

# ---------------------------
# Global exception handler
# ---------------------------
@app.errorhandler(Exception)
def handle_exception(e):
    # Log a full stack trace at error level
    logger.exception("Unhandled exception: %s", e)

    # Increment StatsD counter for exceptions
    # Use a tag-like suffix if you want more granularity, e.g. exceptions.route_boom
    try:
        statsd.incr("exceptions")
        # You can also record a timing or histogram:
        # statsd.timing('exceptions.last_time', 123)
    except Exception as statsd_err:
        # If StatsD itself fails, log the failure but keep going
        logger.error("Failed to send metric to StatsD: %s", statsd_err)

    # Optionally record the exception type as a separate metric
    try:
        ex_name = type(e).__name__
        statsd.incr(f"exceptions.{ex_name}")
    except Exception:
        pass

    # Return a JSON response for the client
    return jsonify({"error": "internal server error", "message": str(e)}), 500

if __name__ == "__main__":
    # Use 0.0.0.0 if you want external access to local container
    app.run(host="0.0.0.0", port=5000, debug=False)
