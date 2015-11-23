import logging
from logging.handlers import TimedRotatingFileHandler

__log_handler_set = False
__log_name_prefix = ""

def set_log_name_prefix(prefix):
    global __log_name_prefix
    _log_name_prefix = prefix

def create_timed_rotating_log():
    """"""
    global __log_name_prefix
    global __log_handler_set
    path = __log_name_prefix + "btcc_collector_logs.txt"
    logger = logging.getLogger(path)
    logger.setLevel(logging.DEBUG)
    if (__log_handler_set == False):
        handler = TimedRotatingFileHandler(path, when="H", interval=1)
        formatter = logging.Formatter('%(asctime)s\t%(pathname)s\t%(levelname)s\t%(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        __log_handler_set = True
    return logger