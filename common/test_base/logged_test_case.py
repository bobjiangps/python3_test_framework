from contextlib import contextmanager
import logging
import datetime
import os


class LoggedTestCase:
    """Test case with a logger"""

    @classmethod
    def setup_class(cls):
        cls.log = logging.getLogger(os.environ.get('PYTEST_CURRENT_TEST').split('::')[-2].split(' ')[0])
        cls.startTime = datetime.datetime.now()
        cls.log.info("Test Suite {0} start".format(cls.__name__))

    def setup_method(self):
        self.log.info("Begin to test {0}.{1}".format(self.__class__.__name__, os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]))

    def teardown_method(self):
        self.log.info("End to test {0}.{1}".format(self.__class__.__name__, os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]))

    @classmethod
    def teardown_class(cls):
        cls.stopTime = datetime.datetime.now()
        runtime = cls.stopTime - cls.startTime
        cls.log.info("Test Suite {0} end, cost time: {1}".format(cls.__name__, str(runtime)))

    @contextmanager
    def precondition(self):
        try:
            yield
        except Exception as e:
            self.log.critical("Exception in precondition")
            self.log.critical(str(e))
            raise e

    @contextmanager
    def steps(self):
        try:
            yield
        except Exception as e:
            self.log.critical("Exception in test steps")
            self.log.critical(str(e))
            raise e

    @contextmanager
    def verify(self):
        try:
            yield
        except Exception as e:
            self.log.critical("Exception in test verification")
            self.log.critical(str(e))
            raise e

    @contextmanager
    def cleanup(self):
        try:
            yield
        except Exception as e:
            self.log.critical("Exception in cleanup")
            self.log.critical(str(e))
            raise e
