from configuration.config import LoadConfig
from utils.email_helper import send_email
import pytest
import os
import datetime


class Application:

    def __init__(self):
        self._config = None
        self._module_cases = {}
        self.start_time = None
        self.end_time = None

    def run(self):
        self.start_time = datetime.datetime.now()
        self._load_config()
        print(self._config)
        report_folder_path = os.path.join(os.getcwd(), "projects", self._config["project"], "test_reports")
        if not os.path.exists(report_folder_path):
            os.mkdir(report_folder_path)
        report_path = os.path.join(report_folder_path, "AutoTest-%s-%s-%s.html" % (self._config["project"], self._config["environment"], datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
        # pytest.main("--html=%s" % report_path) # show warning

        # -v shows the result of each def; -q only shows the overall status; -s shows the print function in test def
        pytest.main(["--html", report_path, "--self-contained-html", "-v"])
        #pytest.main()
        self.end_time = datetime.datetime.now()
        print("Start Time: %s\nEnd Time: %s\nDuraion: %s\nReport file in: %s" % (str(self.start_time), str(self.end_time), str(self.end_time - self.start_time), report_path))
        result_statistics = self._retrieve_result_stat(report_folder_path)
        self._send_test_result(result_statistics, report_path)

    def _load_config(self):
        self._config = LoadConfig.load_config()

    def _retrieve_result_stat(self, report_folder_path):
        result_stat = {"Pass": None, "Fail": None, "Skip": None}
        stat_path = os.path.join(report_folder_path, "stat.csv")
        with open(stat_path, "r") as f:
            for line in f.readlines():
                temp = line.strip().split(",")
                if temp[0] in result_stat.keys():
                    result_stat[temp[0]] = temp[1]
        print(f"result statistics: {str(result_stat)[1:-1]}")
        return str(result_stat)[1:-1]

    def _send_test_result(self, result_statistics, report_file):
        email_setting = dict(self._config["email_sender"], **self._config["email_receiver"][self._config["profile"]])
        email_content = result_statistics
        email_subject = "%s - %s - Auto Test Result" % (self._config["project"], self._config["environment"])
        send_email(email_content, email_subject, email_setting, filename=report_file)
