import logging
from datetime import datetime
from pythonjsonlogger import jsonlogger
from flask import request, has_request_context


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get("timestamp"):
            log_record["timestamp"] = datetime.utcnow()
        if log_record.get("level"):
            log_record["severity"] = log_record["level"].upper()
        else:
            log_record["severity"] = record.levelname
        if has_request_context():
            log_record["user_id"] = request.headers["X-User-Id"]


def init_json_logger():
    logger = logging.getLogger("json_logger")
    log_handler = logging.StreamHandler()
    formatter = CustomJsonFormatter("(timestamp) (severity) (name) (message)")
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG)
