import logging
import sys

class bgcolors:
	PINK = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	END = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

class Logger(object):
    def __init__(self, name="zabbix", level=logging.DEBUG):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.formatter = logging.Formatter("%(levelname)s %(asctime)s - %(message)s")
        # Log to console
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(self.formatter)
        stream_handler.setLevel(logging.ERROR)
        self.logger.addHandler(stream_handler)
        # Log to a file
        #fh = logging.FileHandler("zabbix.log")
        #fh.setFormatter(self.formatter)
        #self.logger.addHandler(fh)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)
        sys.exit(-1)
