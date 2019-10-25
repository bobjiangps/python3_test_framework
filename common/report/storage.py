from configuration.config import LoadConfig
from utils.mysql_helper import MysqlHelper
from utils.geoip_helper import GeoIpHelper
import os
import json
import platform
import time
import datetime


class Storage:

    def __init__(self, round_start_time):
        self._config = None
        self._stat = None
        self.round_start_time = round_start_time
        self.test_type = None
        self.test_type_id = None
        self.device_id = None
        self.mobile_os_id = None
        self.browser_id = None
        self.platform_id = None
        self.project_id = None
        self.environment_id = None
        self.suite_id = None
        self.round_id = None

    def run(self):
        self._load_config()
        db_info = self._config["storage"]
        db_info["host"] = "120.78.133.207"
        # db_info["host"] = "127.0.0.1"
        db_info["username"] = "automation"
        db_info["password"] = "Run_Auto666"
        store_db = MysqlHelper(db_info)
        report_folder_path = os.path.join(os.getcwd(), "projects", self._config["project"], "test_reports")
        stat_file = os.path.join(report_folder_path, "stat.json")
        with open(stat_file, "r") as f:
            self._stat = json.load(f)
        # print(self._config)
        # print(self._stat)
        if self.round_start_time >= datetime.datetime.strptime(self._stat["End_Time"], "%Y-%m-%d-%H:%M:%S.%f"):
            print("No result!! Please check if your skip all cases...")
        else:
            print("Start to record test execution data")
            self.test_type = self.get_test_type()
            self.test_type_id = self.store_test_type(store_db)
            if self.test_type == "Mobile":
                self.device_id = self.store_device_info(store_db)
                self.mobile_os_id = self.store_mobile_os_info(store_db)
            elif self.test_type == "Web":
                self.browser_id = self.store_browser_info(store_db)
            self.platform_id = self.store_platform_info(store_db)
            self.project_id = self.store_project_info(store_db)
            self.environment_id = self.store_environment_info(store_db)
            self.suite_id = self.store_test_script_case_suite_info(store_db)
            # self.suite_id = self.store_test_script_case_suite_info(store_db, "debug_suite")
            self.round_id = self.store_test_round_info(store_db)
            # self.round_id = self.store_test_round_info(store_db, "debug_round")
            self.store_case_result_info(store_db)
            print("Record data complete...")

    def _load_config(self):
        self._config = LoadConfig.load_config()

    def get_test_type(self):
        if self._config["report"]["ui_test"]:
            if self._config["report"]["app_test"]:
                test_type = "Mobile"
            elif self._config["report"]["win_test"]:
                test_type = "Windows"
            else:
                test_type = "Web"
        else:
            if "base_url" in self._config["env"].keys():
                test_type = "Rest"
            else:
                test_type = "API"  # for other types
        return test_type

    def store_test_type(self, db):
        test_type = self.get_test_type()
        test_type_exist_sql = "select * from test_type where name='%s'" % test_type
        test_type_exist = True if len(db.get_all_results_from_database(test_type_exist_sql)) > 0 else False
        if test_type_exist:
            print("test type '%s' already exist in db" % test_type)
        else:
            add_test_type_sql = "INSERT INTO `test_type` VALUES (NULL, '%s')" % test_type
            db.execute_sql(add_test_type_sql, commit=True)
            print("add new test type '%s' in db" % test_type)
        return db.get_all_results_from_database(test_type_exist_sql)[-1]["id"]

    def store_browser_info(self, db):
        alias = {
            "Chrome": "chrome",
            "Firefox": "firefox",
            "Safari": "Safari",
            "IE": "internet explorer",
            "Edge": "MicrosoftEdge",
            "MobileBrowser": "chrome"
        }
        browser_name = self._config["browser"]
        browser_version = self._stat["browser_version"]
        browser_exist_sql = "select * from browser where name='%s' and version='%s'" % (browser_name, browser_version)
        browser_exist = True if len(db.get_all_results_from_database(browser_exist_sql)) > 0 else False
        if browser_exist:
            print("browser '%s - %s' already exist in db" % (browser_name, browser_version))
        else:
            add_browser_sql = "INSERT INTO `browser` VALUES (NULL, '%s', '%s', '%s', CURRENT_TIME(), CURRENT_TIME())" % (browser_name, alias[browser_name], browser_version)
            db.execute_sql(add_browser_sql, commit=True)
            print("add new browser '%s - %s' in db" % (browser_name, browser_version))
        return db.get_all_results_from_database(browser_exist_sql)[-1]["id"]

    def store_mobile_os_info(self, db):
        mobile_os_name = self._config["mobile"]
        mobile_os_version = self._stat["mobile_platform_version"]
        mobile_os_exist_sql = "select * from mobile_os where name='%s' and version='%s'" % (mobile_os_name, mobile_os_version)
        mobile_os_exist = True if len(db.get_all_results_from_database(mobile_os_exist_sql)) > 0 else False
        if mobile_os_exist:
            print("mobile os '%s - %s' already exist in db" % (mobile_os_name, mobile_os_version))
        else:
            add_mobile_os_sql = "INSERT INTO `mobile_os` VALUES (NULL, '%s', '%s', CURRENT_TIME(), CURRENT_TIME())" % (mobile_os_name, mobile_os_version)
            db.execute_sql(add_mobile_os_sql, commit=True)
            print("add new mobile os '%s - %s' in db" % (mobile_os_name, mobile_os_version))
        return db.get_all_results_from_database(mobile_os_exist_sql)[-1]["id"]

    def store_device_info(self, db):
        device = self._config["device"]
        device_exist_sql = "select * from device where name='%s'" % device
        device_exist = True if len(db.get_all_results_from_database(device_exist_sql)) > 0 else False
        if device_exist:
            print("device '%s' already exist in db" % device)
        else:
            add_device_sql = "INSERT INTO `device` VALUES (NULL, '%s', CURRENT_TIME(), CURRENT_TIME())" % device
            db.execute_sql(add_device_sql, commit=True)
            print("add new device '%s' in db" % device)
        return db.get_all_results_from_database(device_exist_sql)[-1]["id"]

    @staticmethod
    def store_platform_info(db):
        platform_version = platform.platform()
        if platform_version.lower().find("windows") >= 0:
            platform_name = "Windows"
        elif platform_version.lower().find("darwin") >= 0:
            platform_name = "Macos"
        elif platform_version.lower().find("linux") >= 0:
            platform_name = "Linux"
        else:
            platform_name = "unknown"
        platform_exist_sql = "select * from platform_os where name='%s' and version='%s'" % (platform_name, platform_version)
        platform_exist = True if len(db.get_all_results_from_database(platform_exist_sql)) > 0 else False
        if platform_exist:
            print("platform '%s - %s' already exist in db" % (platform_name, platform_version))
        else:
            add_platform_sql = "INSERT INTO `platform_os` VALUES (NULL, '%s', '%s', CURRENT_TIME(), CURRENT_TIME())" % (platform_name, platform_version)
            db.execute_sql(add_platform_sql, commit=True)
            print("add platform '%s - %s' in db" % (platform_name, platform_version))
        return db.get_all_results_from_database(platform_exist_sql)[-1]["id"]

    def store_project_info(self, db):
        project = self._config["project"]
        project_exist_sql = "select * from project where name='%s'" % project
        project_exist = True if len(db.get_all_results_from_database(project_exist_sql)) > 0 else False
        if project_exist:
            print("project '%s' already exist in db" % project)
        else:
            add_project_sql = "INSERT INTO `project` VALUES (NULL, '%s', CURRENT_TIME(), CURRENT_TIME())" % project
            db.execute_sql(add_project_sql, commit=True)
            print("add new project '%s' in db" % project)
        return db.get_all_results_from_database(project_exist_sql)[-1]["id"]

    def store_environment_info(self, db):
        environment = self._config["environment"]
        environment_exist_sql = "select * from test_environment where name='%s'" % environment
        environment_exist = True if len(db.get_all_results_from_database(environment_exist_sql)) > 0 else False
        if environment_exist:
            print("environment '%s' already exist in db" % environment)
        else:
            add_environment_sql = "INSERT INTO `test_environment` VALUES (NULL, '%s')" % environment
            db.execute_sql(add_environment_sql, commit=True)
            print("add new test environment '%s' in db" % environment)
        return db.get_all_results_from_database(environment_exist_sql)[-1]["id"]

    def store_test_script_case_suite_info(self, db, test_suite_name=None):
        if not test_suite_name:
            test_suite_name = "Suite%s" % time.strftime("%Y%m%d%H%M%S", time.localtime())
        suite_exist_sql = "select * from test_suite where name = '%s'" % test_suite_name
        suite_exist = True if len(db.get_all_results_from_database(suite_exist_sql)) > 0 else False
        if suite_exist:
            print("suite '%s' already exist in db" % test_suite_name)
        else:
            add_suite_sql = "INSERT INTO `test_suite` VALUES (NULL, '%s', CURRENT_TIME(), CURRENT_TIME())" % test_suite_name
            db.execute_sql(add_suite_sql, commit=True)
            print("add new test suite '%s' in db" % test_suite_name)
        test_suite_id = db.get_all_results_from_database(suite_exist_sql)[-1]["id"]

        scripts = self._stat["Cases"].keys()
        for s in scripts:
            script_exist_sql = "select * from test_script where name = '%s'" % s
            script_exist = True if len(db.get_all_results_from_database(script_exist_sql)) > 0 else False
            if not script_exist:
                add_script_sql = "INSERT INTO `test_script` VALUES (NULL, '%s', CURRENT_TIME(), CURRENT_TIME())" % s
                db.execute_sql(add_script_sql, commit=True)
                print("add new script '%s' in db" % s)
            test_script_id = db.get_all_results_from_database(script_exist_sql)[-1]["id"]

            script_functions = self._stat["Cases"][s].keys()
            for f in script_functions:
                function_exist_sql = "select * from test_function where name = '%s'" % f
                function_exist = True if len(db.get_all_results_from_database(function_exist_sql)) > 0 else False
                if not function_exist:
                    add_function_sql = "INSERT INTO `test_function` VALUES (NULL, '%s', %s, CURRENT_TIME(), CURRENT_TIME())" % (f, test_script_id)
                    db.execute_sql(add_function_sql, commit=True)
                    print("add new function '%s' in db" % f)
                test_function_id = db.get_all_results_from_database(function_exist_sql)[-1]["id"]

                case_name = self._stat["Cases"][s][f]
                case_exist_sql = "select * from test_case where name = '%s'" % case_name
                case_exist = True if len(db.get_all_results_from_database(case_exist_sql)) > 0 else False
                if not case_exist:
                    add_case_sql = "INSERT INTO `test_case` VALUES (NULL, '%s', %s, CURRENT_TIME(), CURRENT_TIME())" % (case_name, test_function_id)
                    db.execute_sql(add_case_sql, commit=True)
                    print("add new case '%s' in db" % case_name)
                test_case_id = db.get_all_results_from_database(case_exist_sql)[-1]["id"]

                case_suite_exist_sql = "select * from case_suite where test_suite_id = %s and test_case_id = %s" % (test_suite_id, test_case_id)
                case_suite_exist = True if len(db.get_all_results_from_database(case_suite_exist_sql)) > 0 else False
                if not case_suite_exist:
                    add_case_suite_sql = "INSERT INTO `case_suite` VALUES (NULL, %s, %s, CURRENT_TIME(), CURRENT_TIME())" % (test_suite_id, test_case_id)
                    db.execute_sql(add_case_suite_sql, commit=True)
                    # print("add new case suite relation '%s - %s' in db" % (test_suite_id, test_case_id))
        print("add new case suite relation in db")
        return test_suite_id

    def store_test_round_info(self, db, test_round_name=None):
        if not test_round_name:
            test_round_name = "Round%s" % time.strftime("%Y%m%d%H%M%S", time.localtime())
        round_exist_sql = "select * from test_round where name = '%s'" % test_round_name
        round_exist = True if len(db.get_all_results_from_database(round_exist_sql)) > 0 else False
        if round_exist:
            print("round '%s' already exist in db" % test_round_name)
            test_round_name += time.strftime("%Y%m%d%H%M%S", time.localtime())
            print("change to a new round name '%s'" % test_round_name)
        ip = GeoIpHelper.get_ip()
        location = GeoIpHelper.get_location(ip)
        if self.test_type == "Mobile":
            add_round_sql = "INSERT INTO `test_round` VALUES (NULL, '%s', %s, NULL, %s, %s, %s, %s, %s, '%s', '%s', CURRENT_TIME(), CURRENT_TIME())" % (test_round_name, self.suite_id, self.device_id, self.mobile_os_id, self.platform_id, self.environment_id, self.test_type_id, ip, location)
        elif self.test_type == "Web":
            add_round_sql = "INSERT INTO `test_round` VALUES (NULL, '%s', %s, %s, NULL, NULL, %s, %s, %s, '%s', '%s', CURRENT_TIME(), CURRENT_TIME())" % (test_round_name, self.suite_id, self.browser_id, self.platform_id, self.environment_id, self.test_type_id, ip, location)
        else:
            add_round_sql = "INSERT INTO `test_round` VALUES (NULL, '%s', %s, NULL, NULL, NULL, %s, %s, %s, '%s', '%s', CURRENT_TIME(), CURRENT_TIME())" % (test_round_name, self.suite_id, self.platform_id, self.environment_id, self.test_type_id, ip, location)
        db.execute_sql(add_round_sql, commit=True)
        print("add new test round '%s' in db" % test_round_name)
        return db.get_all_results_from_database("select * from test_round where name = '%s'" % test_round_name)[-1]["id"]

    def store_case_result_info(self, db):
        details = self._stat["Details"]
        failures = self._stat["Failures"]
        for s in details.keys():
            for f in details[s].keys():
                result = details[s][f]
                data_driven = None
                f_split = f.split("[")
                function_name = f_split[0]
                if len(f_split) > 1:
                    data_driven = f_split[1].split("]")[0]
                test_case_id_sql = "SELECT tc.id FROM `test_case` as tc " \
                                   "left join `test_function` as tf on tc.test_function_id = tf.id " \
                                   "left join `test_script` as ts on tf.script_id = ts.id " \
                                   "where tf.name='%s' and ts.name='%s'" % (function_name, s)
                test_case_id = db.get_all_results_from_database(test_case_id_sql)[-1]["id"]
                if result == "fail":
                    error_message = failures[s][f]["error_message"]
                    if "screenshot" in failures[s][f].keys():
                        screenshot = failures[s][f]["screenshot"]
                        if data_driven:
                            add_case_result_sql = "INSERT INTO `test_case_result` VALUES (NULL, %s, %s, '%s', '%s', NULL, '%s', '%s', CURRENT_TIME(), CURRENT_TIME())" % (test_case_id, self.round_id, error_message.replace("'", '"'), screenshot, result, data_driven)
                        else:
                            add_case_result_sql = "INSERT INTO `test_case_result` VALUES (NULL, %s, %s, '%s', '%s', NULL, '%s', NULL, CURRENT_TIME(), CURRENT_TIME())" % (test_case_id, self.round_id, error_message.replace("'", '"'), screenshot, result)
                            print(add_case_result_sql)
                    else:
                        if data_driven:
                            add_case_result_sql = "INSERT INTO `test_case_result` VALUES (NULL, %s, %s, '%s', NULL, NULL, '%s', '%s', CURRENT_TIME(), CURRENT_TIME())" % (test_case_id, self.round_id, error_message.replace("'", '"'), result, data_driven)
                        else:
                            add_case_result_sql = "INSERT INTO `test_case_result` VALUES (NULL, %s, %s, '%s', NULL, NULL, '%s', NULL, CURRENT_TIME(), CURRENT_TIME())" % (test_case_id, self.round_id, error_message.replace("'", '"'), result)
                else:
                    if data_driven:
                        add_case_result_sql = "INSERT INTO `test_case_result` VALUES (NULL, %s, %s, NULL, NULL, NULL, '%s', '%s', CURRENT_TIME(), CURRENT_TIME())" % (test_case_id, self.round_id, result, data_driven)
                    else:
                        add_case_result_sql = "INSERT INTO `test_case_result` VALUES (NULL, %s, %s, NULL, NULL, NULL, '%s', NULL, CURRENT_TIME(), CURRENT_TIME())" % (test_case_id, self.round_id, result)
                db.execute_sql(add_case_result_sql, commit=True)
        print("add new test case result in db")
