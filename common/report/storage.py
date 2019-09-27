from configuration.config import LoadConfig
from utils.mysql_helper import MysqlHelper
from utils.geoip_helper import GeoIpHelper
import os
import json
import platform


class Storage:

    def __init__(self):
        self._config = None
        self._stat = None

    def run(self):
        print("Start to record test execution data")
        self._load_config()
        db_info = self._config["storage"]
        # db_info["host"] = "120.78.133.207"
        db_info["host"] = "127.0.0.1"
        db_info["username"] = "automation"
        db_info["password"] = "Run_Auto666"
        store_db = MysqlHelper(db_info)
        report_folder_path = os.path.join(os.getcwd(), "projects", self._config["project"], "test_reports")
        stat_file = os.path.join(report_folder_path, "stat.json")
        with open(stat_file, "r") as f:
            self._stat = json.load(f)
        print(self._config)
        print(self._stat)
        test_type = self.get_test_type()
        test_type_id = self.store_test_type(store_db)
        if test_type == "Mobile":
            device_id = self.store_device_info(store_db)
            mobile_os_id = self.store_mobile_os_info(store_db)
        elif test_type == "Web":
            browser_id = self.store_browser_info(store_db)
        platform_id = self.store_platform_info(store_db)
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
