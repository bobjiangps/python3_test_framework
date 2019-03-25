from configuration.config import LoadConfig
from utils.email_helper import send_email
import pytest
import os
import datetime


class Application:

    def __init__(self):
        self._config = None
        self._module_cases = {}

    def run(self):
        self._load_config()
        print(self._config)
        report_folder_path = os.path.join(os.getcwd(), "projects", self._config["project"], "test_reports")
        if not os.path.exists(report_folder_path):
            os.mkdir(report_folder_path)
        report_path = os.path.join(report_folder_path, "AutoTest-%s-%s-%s.html" % (self._config["project"], self._config["environment"], datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
        print(report_path)
        # pytest.main("--html=%s" % report_path) # show warning

        # -v shows the result of each def; -q only shows the overall status; -s shows the print function in test def
        pytest.main(["--html", report_path, "--self-contained-html", "-v"])
        #pytest.main()
        #self._send_test_result()

    def _load_config(self):
        self._config = LoadConfig.load_config()

    def _send_test_result(self):
        email_setting = dict(self._config["email_sender"], **self._config["email_receiver"][self._config["profile"]])
        email_content = "test content"
        email_subject = "%s - %s - Auto Test Result" % (self._config["project"], self._config["environment"])
        send_email(email_content, email_subject, email_setting)
