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
        log_folder_path = os.path.join(os.getcwd(), "projects", self._config["project"], "log")
        data_folder_path = os.path.join(os.getcwd(), "projects", self._config["project"], "test_data")
        for folder in [report_folder_path, log_folder_path, data_folder_path]:
            if not os.path.exists(folder):
                os.mkdir(folder)
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

        # -v shows the result of each def; -q only shows the overall status; -s shows the print function in test def
        command_list = ["--html", report_path, "--self-contained-html", "-v", "--tb=short"]
        # if has include_test, then run these cases; else check and run exclude_test
        if self._config["test"]:
            for in_test in self._config["test"].split(","):
                command_list.append(os.path.join("projects", self._config["project"], "tests", in_test.strip()))
        elif not self._config["test"]:
            command_list.append(os.path.join("projects", self._config["project"], "tests"))
        elif self._config["exclude_test"]:
            for ex_test in self._config["exclude_test"].split(","):
                command_list.append("--deselect")
                command_list.append(os.path.join("projects", self._config["project"], "tests", ex_test.strip()))
        # run tests which name match keyword, example: keyword, not keyword, key1 or key2, key1 and key2
        if self._config["keyword"]:
            command_list.append("-k")
            command_list.append(self._config["keyword"].strip())
        # run tests which name match marker, example: marker, not marker, marker1 or marker2, marker1 and marker2
        if self._config["marker"]:
            command_list.append("-m")
            command_list.append(self._config["marker"].strip())
        # rerun failures
        if self._config["rerun"]["rerun_times"]:
            command_list.append("--reruns")
            command_list.append(str(self._config["rerun"]["rerun_times"]))
            if self._config["rerun"]["rerun_delay"]:
                command_list.append("--reruns-delay")
                command_list.append(str(self._config["rerun"]["rerun_delay"]))
        # log
        #command_list.append('--log-format="%(asctime)s %(levelname)s %(message)s"')
        #command_list.append('--log-date-format="%Y-%m-%d %H:%M:%S"')
        #command_list.append("--show-capture=no")
        command_list.append("--log-file=%s" % os.path.join(os.getcwd(), "projects", LoadConfig.load_config()["project"], "log", "AutoTest-%s.log" % datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
        pytest.main(command_list)
        # print(command_list)
        self.end_time = datetime.datetime.now()
        print("Start Time: %s\nEnd Time: %s\nDuraion: %s\nReport file in: %s" % (str(self.start_time), str(self.end_time), str(self.end_time - self.start_time), report_path))
        result_statistics = self._generate_result_statistics(report_folder_path, self.start_time)
        self._send_test_result(result_statistics, report_path)
        self.exit_test()

    def _load_config(self):
        self._config = LoadConfig.load_config()

    def _generate_result_statistics(self, report_folder_path, start_time):
        result_stat = {"Total": None, "Pass": None, "Fail": None, "Skip": None, "End_Time": None}
        stat_path = os.path.join(report_folder_path, "stat.json")
        with open(stat_path, "r") as f:
            result_json = json.load(f)
            for item in result_json.keys():
                if item in result_stat.keys():
                    result_stat[item] = result_json[item]
        if start_time >= datetime.datetime.strptime(result_stat["End_Time"], "%Y-%m-%d-%H:%M:%S.%f"):
            print("No result!! Please check if your skip all cases...")
            return False
        else:
            print(f"Overall Result Statistics: {str(result_stat)[1:-1]}")
            self._module_cases = {}
            fail_skip_suite = {"has_fail": [], "has_skip": []}
            for item in result_json["Details"].items():
                self._module_cases[item[0]] = {"case_total": 0, "case_pass": 0, "case_fail": 0, "case_skip": 0}
                for v in item[1].values():
                    self._module_cases[item[0]]["case_total"] += 1
                    if v.lower() == "pass":
                        self._module_cases[item[0]]["case_pass"] += 1
                    elif v.lower() == "fail":
                        self._module_cases[item[0]]["case_fail"] += 1
                        # if has fail and skip, mark it as has_fail
                        if item[0] not in fail_skip_suite["has_fail"]:
                            fail_skip_suite["has_fail"].append(item[0])
                    elif v.lower() == "skip":
                        self._module_cases[item[0]]["case_skip"] += 1
                        if item[0] not in fail_skip_suite["has_skip"]:
                            fail_skip_suite["has_skip"].append(item[0])

            stat_template = os.path.join(os.getcwd(), "common", "report", "statistics.html")
            with open(stat_template) as f:
                statistics = f.read()
            statistics = statistics.replace("<strong>Project:</strong></p>", "<strong>Project:</strong> %s</p>" % self._config["project"])
            statistics = statistics.replace("<strong>Environment:</strong></p>", "<strong>Environment:</strong> %s</p>" % self._config["environment"])
            statistics = statistics.replace("<strong>Start Time:</strong></p>", "<strong>Start Time:</strong> %s</p>" % str(self.start_time)[:-7])
            statistics = statistics.replace("<strong>Duration:</strong></p>", "<strong>Duration:</strong> %s</p>" % str(self.end_time - self.start_time)[:-7])
            statistics = statistics.replace("<td>total_suite</td><td>total_case</td>", "<td>%d</td><td>%d</td>" % (len(self._module_cases.keys()), result_stat["Total"]))
            statistics = statistics.replace("<td>pass_suite</td><td>pass_case</td>", "<td>%d</td><td>%d</td>" % ((len(self._module_cases.keys()) - len(fail_skip_suite["has_fail"]) - len(fail_skip_suite["has_skip"])), result_stat["Pass"]))
            statistics = statistics.replace("<td>fail_suite</td><td>fail_case</td>", "<td>%d</td><td>%d</td>" % (len(fail_skip_suite["has_fail"]), result_stat["Fail"]))
            statistics = statistics.replace("<td>skip_suite</td><td>skip_case</td>", "<td>%d</td><td>%d</td>" % (len(fail_skip_suite["has_skip"]), result_stat["Skip"]))
            modules_stat_string = ""
            for item in self._module_cases.items():
                modules_stat_string += "<tr class='module-row'><td>%s</td><td>%d</td><td class='pass-cell'>%d</td><td class='fail-cell'>%d</td><td class='skip-cell'>%d</td></tr>" % (item[0], item[1]["case_total"], item[1]["case_pass"], item[1]["case_fail"], item[1]["case_skip"])
            statistics = statistics.replace("<tr class='module-row'></tr>", modules_stat_string)
            return statistics

    def _send_test_result(self, result_statistics, report_file):
        if result_statistics:
            email_setting = dict(self._config["email_sender"], **self._config["email_receiver"][self._config["profile"]])
            email_content = result_statistics
            email_subject = "%s - %s - Auto Test Result" % (self._config["project"], self._config["environment"])
            print(f"Send email: {email_subject}")
            send_email(email_content, email_subject, email_setting, filename=report_file)

    def exit_test(self):
        print("Test Complete...\n")
