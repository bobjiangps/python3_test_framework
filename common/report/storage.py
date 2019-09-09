from configuration.config import LoadConfig
import os
import json


class Storage:

    def __init__(self):
        self._config = None
        self._stat = None

    def run(self):
        self._load_config()
        report_folder_path = os.path.join(os.getcwd(), "projects", self._config["project"], "test_reports")
        stat_file = os.path.join(report_folder_path, "stat.json")
        with open(stat_file, "r") as f:
            self._stat = json.load(f)

    def _load_config(self):
        self._config = LoadConfig.load_config()
