from configuration.config import LoadConfig
from utils.mysql_helper import MysqlHelper
import os
import json


class Storage:

    def __init__(self):
        self._config = None
        self._stat = None

    def run(self):
        self._load_config()
        db_info = self._config["storage"]
        db_info["host"] = "120.78.133.207"
        db_info["username"] = "automation"
        db_info["password"] = "Run_Auto666"
        store_db = MysqlHelper(db_info)
        report_folder_path = os.path.join(os.getcwd(), "projects", self._config["project"], "test_reports")
        stat_file = os.path.join(report_folder_path, "stat.json")
        with open(stat_file, "r") as f:
            self._stat = json.load(f)

    def _load_config(self):
        self._config = LoadConfig.load_config()
