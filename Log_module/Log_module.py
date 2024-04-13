import logging
import logging.handlers
import time
import os
import sys


# This module should be used in >=3.4 version


class MyLogger(object):
    """Create my self.log from python stdlib self.log module"""
    def __init__(self):
        self.log = logging.getLogger('Mark01')
        self.log.setLevel(logging.DEBUG)
        LOG_PATH = os.getcwd()
        # Console stream output:
        stream_handler = logging.StreamHandler(stream=sys.stderr)
        stream_handler.setFormatter(logging.Formatter("%(asctime)s "
                                                      "\n- ProcessId: %(process)d "
                                                      "\n- ThreadId: %(thread)d "
                                                      "\n- Level: %(levelname)s "
                                                      "\n- FictionName: %(funcName)s "
                                                      "\n- Message:\n------%(message)s\n"))
        stream_handler.setLevel(logging.INFO)
        # File stream output:
        file_handler = logging.handlers.TimedRotatingFileHandler('logfile',
                                                                 when='M',
                                                                 interval=1,
                                                                 backupCount=10,
                                                                 delay=True)
        file_handler.suffix = "%Y-%m-%d_%H-%M-%S.txt"
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter("%(asctime)s "
                                                    "\n- ProcessId:%(process)d "
                                                    "\n- ThreadId:%(thread)d "
                                                    "\n- ThreadName:%(threadName)s "
                                                    "\n- Level:%(levelname)s "
                                                    "\n- FictionName:%(funcName)s "
                                                    "\nMessage:\n------%(message)s\n"))
        self.log.addHandler(file_handler)
        self.log.addHandler(stream_handler)
        self.log.info('self.log has benn initialized')
        self.log.info(f'LOG_PATH is {LOG_PATH}')