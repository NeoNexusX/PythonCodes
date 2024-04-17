import logging
import logging.handlers
import time
import os
import sys
from logging.handlers import TimedRotatingFileHandler


# This module should be used in >=3.4 version


class MyLogger(logging.Logger):
    """Create my self.log from python stdlib self.log module"""

    def __init__(self):
        # 使用 Logger 的名称初始化 Logger 对象
        super().__init__('FuJian Cancer Project')

        # 设置日志级别
        self.setLevel(logging.DEBUG)

        # 获取当前工作目录
        LOG_PATH = os.getcwd()

        # 控制台输出处理器
        stream_handler = logging.StreamHandler(stream=sys.stderr)
        stream_handler.setFormatter(logging.Formatter("%(asctime)s "
                                                      "\n- ProcessId: %(process)d "
                                                      "\n- ThreadId: %(thread)d "
                                                      "\n- Level: %(levelname)s "
                                                      "\n- FileName:%(filename)s "
                                                      "\n- Lineno:%(lineno)d "
                                                      "\n- FunctionName: %(funcName)s "
                                                      "\n- Message:\n--------\n%(message)s\n--------\n"))
        stream_handler.setLevel(logging.DEBUG)

        # 文件输出处理器
        file_handler = TimedRotatingFileHandler('logfile',
                                                when='S',
                                                interval=60,
                                                backupCount=2,
                                                delay=True)
        file_handler.suffix = "%Y-%m-%d_%H-%M-%S.txt"
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter("%(asctime)s "
                                                    "\n- ProcessId:%(process)d "
                                                    "\n- ThreadId:%(thread)d "
                                                    "\n- ThreadName:%(threadName)s "
                                                    "\n- Level:%(levelname)s "
                                                    "\n- FileName:%(filename)s "
                                                    "\n- Lineno:%(lineno)d "
                                                    "\n- FunctionName:%(funcName)s "
                                                      "\n- Message:\n--------\n%(message)s\n--------\n"))

        # 将处理器添加到 Logger
        self.addHandler(file_handler)
        self.addHandler(stream_handler)

        # 记录日志消息
        self.info('Logger has been initialized')
        self.info(f'LOG_PATH is {LOG_PATH}')
