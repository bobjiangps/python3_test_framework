from configuration.config import LoadConfig
from utils.email_helper import send_email
import pytest
import os
import datetime
import json


class Application:

    def __init__(self):
        self._config = None
        self._module_cases = {}
        self.start_time = None
        self.end_time = None

    def run(self):
        self.start_time = datetime.datetime.now()
        self._load_config()
        # print(self._config)
        report_folder_path = os.path.join(os.getcwd(), "projects", self._config["project"], "test_reports")
        if not os.path.exists(report_folder_path):
            os.mkdir(report_folder_path)
        if self._config["report"]["ui_test"]:
            if self._config["report"]["app_test"]:
                report_suffix = self._config["mobile"]
            elif self._config["report"]["win_test"]:
                report_suffix = "WindowsSoftware"
            else:
                report_suffix = self._config["browser"]
        else:
            report_suffix = "API"
        report_path = os.path.join(report_folder_path, "AutoTest-%s-%s-%s-%s.html" % (self._config["project"], self._config["environment"], report_suffix, datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
        # pytest.main("--html=%s" % report_path) # show warning

        # -v shows the result of each def; -q only shows the overall status; -s shows the print function in test def
        pytest.main(["--html", report_path, "--self-contained-html", "-v"])
        # pytest.main()

        self.end_time = datetime.datetime.now()
        print("Start Time: %s\nEnd Time: %s\nDuraion: %s\nReport file in: %s" % (str(self.start_time), str(self.end_time), str(self.end_time - self.start_time), report_path))
        result_statistics = self._generate_result_statistics(report_folder_path)
        self._send_test_result(result_statistics, report_path)

    def _load_config(self):
        self._config = LoadConfig.load_config()

    def _generate_result_statistics(self, report_folder_path):
        result_stat = {"Total": None, "Pass": None, "Fail": None, "Skip": None}
        stat_path = os.path.join(report_folder_path, "stat.json")
        with open(stat_path, "r") as f:
            result_json = json.load(f)
            for item in result_json.keys():
                if item in result_stat.keys():
                    result_stat[item] = result_json[item]
        print(f"Overall Result Statistics: {str(result_stat)[1:-1]}")
        modules_cases = {}
        fail_skip_suite = {"has_fail": [], "has_skip": []}
        for item in result_json["Details"].items():
            modules_cases[item[0]] = {"case_total": 0, "case_pass": 0, "case_fail": 0, "case_skip": 0}
            for v in item[1].values():
                modules_cases[item[0]]["case_total"] += 1
                if v.lower() == "pass":
                    modules_cases[item[0]]["case_pass"] += 1
                elif v.lower() == "fail":
                    modules_cases[item[0]]["case_fail"] += 1
                    # if has fail and skip, mark it as has_fail
                    if item[0] not in fail_skip_suite["has_fail"]:
                        fail_skip_suite["has_fail"].append(item[0])
                elif v.lower() == "skip":
                    modules_cases[item[0]]["case_skip"] += 1
                    if item[0] not in fail_skip_suite["has_skip"]:
                        fail_skip_suite["has_skip"].append(item[0])

        stat_template = os.path.join(os.getcwd(), "common", "report", "statistics.html")
        with open(stat_template) as f:
            statistics = f.read()
        statistics = statistics.replace("<strong>Project:</strong></p>", "<strong>Project:</strong> %s</p>" % self._config["project"])
        statistics = statistics.replace("<strong>Environment:</strong></p>", "<strong>Environment:</strong> %s</p>" % self._config["environment"])
        statistics = statistics.replace("<strong>Start Time:</strong></p>", "<strong>Start Time:</strong> %s</p>" % str(self.start_time)[:-7])
        statistics = statistics.replace("<strong>Duration:</strong></p>", "<strong>Duration:</strong> %s</p>" % str(self.end_time - self.start_time)[:-7])
        statistics = statistics.replace("<td>total_suite</td><td>total_case</td>", "<td>%d</td><td>%d</td>" % (len(modules_cases.keys()), result_stat["Total"]))
        statistics = statistics.replace("<td>pass_suite</td><td>pass_case</td>", "<td>%d</td><td>%d</td>" % ((len(modules_cases.keys()) - len(fail_skip_suite["has_fail"]) - len(fail_skip_suite["has_skip"])), result_stat["Pass"]))
        statistics = statistics.replace("<td>fail_suite</td><td>fail_case</td>", "<td>%d</td><td>%d</td>" % (len(fail_skip_suite["has_fail"]), result_stat["Fail"]))
        statistics = statistics.replace("<td>skip_suite</td><td>skip_case</td>", "<td>%d</td><td>%d</td>" % (len(fail_skip_suite["has_skip"]), result_stat["Skip"]))
        modules_stat_string = ""
        for item in modules_cases.items():
            modules_stat_string += "<tr class='module-row'><td>%s</td><td>%d</td><td class='pass-cell'>%d</td><td class='fail-cell'>%d</td><td class='skip-cell'>%d</td></tr>" % (item[0], item[1]["case_total"], item[1]["case_pass"], item[1]["case_fail"], item[1]["case_skip"])
        statistics = statistics.replace("<tr class='module-row'></tr>", modules_stat_string)
        return statistics

    def _send_test_result(self, result_statistics, report_file):
        email_setting = dict(self._config["email_sender"], **self._config["email_receiver"][self._config["profile"]])
        email_content = result_statistics
        email_subject = "%s - %s - Auto Test Result" % (self._config["project"], self._config["environment"])
        send_email(email_content, email_subject, email_setting, filename=report_file)
