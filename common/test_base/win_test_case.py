from utils.winauto_helper import WinautoHelper
from utils.yaml_helper import YamlHelper
from configuration.config import LoadConfig
from common.test_base.logged_test_case import LoggedTestCase
from utils.video_helper import VideoHelper
import os
import json
import datetime


class WinTestCase(LoggedTestCase):
    """Test case for testing windows application"""

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.start_app()

    @classmethod
    def teardown_class(cls):
        super().teardown_class()
        WinautoHelper.close_driver()

    def setup_method(self):
        super().setup_method()
        self.video_config = LoadConfig.load_config("video")
        if self.video_config["record"]:
            video_folder_path = os.path.join(os.getcwd(), "projects", LoadConfig.load_config("project"), "test_reports", "videos")
            if not os.path.exists(video_folder_path):
                os.mkdir(video_folder_path)
            self.video_file_path = os.path.join(video_folder_path, "%s.mp4" % datetime.datetime.now().strftime("%Y%m%d%H%M%S%f"))
            self.vh = VideoHelper(out_file=self.video_file_path)
            self.vh.start_recording_screen()
        self.browser_home_page()

    def teardown_method(self):
        super().teardown_method()
        if self.video_config["record"]:
            self.vh.stop_recording_screen()
            self.log.info("video captured")
            if self.video_config["only_record_failed"]:
                stat_file = os.path.join(os.getcwd(), "projects", LoadConfig.load_config("project"), "test_reports", "stat.json")
                with open(stat_file, "r") as f:
                    current_stat = json.load(f)
                current_test = os.environ.get('PYTEST_CURRENT_TEST').split('::')
                current_test_file = current_test[0].split(os.sep)[-1].split(".")[0]
                current_test_name = current_test[-1].split(" ")[0]
                if current_stat["Details"][current_test_file][current_test_name].lower() == "pass":
                    os.remove(self.video_file_path)
                    self.log.info("remove video because current test pass")

    @classmethod
    def start_app(cls):
        project = LoadConfig.load_config()["project"]
        executable = LoadConfig.load_config()["env"]["executable"]
        win_caps_file = os.path.join(os.getcwd(), "projects", project, "conf", "win_caps.yaml")
        if os.path.exists(win_caps_file):
            win_caps = YamlHelper.load_yaml(win_caps_file)
            cls._driver = WinautoHelper.get_driver(executable, win_caps)
        else:
            cls._driver = WinautoHelper.get_driver(executable)

    @classmethod
    def restart_app(cls):
        WinautoHelper.close_driver()
        cls.start_app()
