from configuration.config import LoadConfig
import logging
import sys
import os


class LoggingHelper:

    @classmethod
    def get_handler(cls, level=logging.DEBUG, stream=sys.stdout):
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        stdout_handler = logging.StreamHandler(stream)
        stdout_handler.setLevel(level)
        stdout_handler.setFormatter(formatter)
        return stdout_handler

    @classmethod
    def add_handler(cls, logger, handler):
        return logger.addHandler(handler)

    @classmethod
    def remove_handler(cls, logger, handler):
        return logger.removeHandler(handler)

    @classmethod
    def initialize_logger(cls, logger):
        logging.basicConfig(level=LoadConfig.load_config()["log_level"],
                            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                            filename=os.path.join(os.getcwd(), "projects", LoadConfig.load_config()["project"], "log", "AutoTest.log"),
                            filemode='a')

        if len(logger.handlers) == 0:
            cls.add_handler(logger, cls.get_handler(level=LoadConfig.load_config()["log_level"]))
        else:
            logger.setLevel(LoadConfig.load_config()["log_level"])
        return logger
    





