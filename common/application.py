from configuration.config import LoadConfig
from utils.email_helper import send_email
import pytest


class Application:

    def __init__(self):
        self._config = None
        self._module_cases = {}

    def run(self):
        self._load_config()
        print(self._config)
        pytest.main()
        self._send_test_result()

    def _load_config(self):
        self._config = LoadConfig.load_config()

    def _send_test_result(self):
        email_setting = dict(self._config["email_sender"], **self._config["email_receiver"][self._config["profile"]])
        email_content = "test content"
        email_subject = "%s - %s - Auto Test Result" % (self._config["project"],self._config["environment"])
        send_email(email_content, email_subject, email_setting)