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
        self.store_test_type(store_db)
        self.store_platform_info(store_db)
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
            db.execute_sql(add_test_type_sql)
            print("add new test type '%s' in db" % test_type)

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
            db.execute_sql(add_platform_sql)
            print("add platform '%s - %s' in db" % (platform_name, platform_version))
