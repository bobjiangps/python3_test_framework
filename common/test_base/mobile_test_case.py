from utils.appium_helper import AppiumHelper
from utils.yaml_helper import YamlHelper
from utils.stf_helper import StfDevices
from configuration.config import LoadConfig
from common.test_base.logged_test_case import LoggedTestCase
import os
import base64
import datetime
import json


class MobileTestCase(LoggedTestCase):
    """Test case for testing mobile application"""

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.start_app()

    def setup_method(self):
        super().setup_method()
        self.video_config = LoadConfig.load_config("video")
        if self.video_config["record"]:
            self._driver.start_recording_screen()

    def teardown_method(self):
        super().teardown_method()
        if self.video_config["record"]:
            video = self._driver.stop_recording_screen()
            video_folder_path = os.path.join(os.getcwd(), "projects", LoadConfig.load_config("project"), "test_reports", "videos")
            if not os.path.exists(video_folder_path):
                os.mkdir(video_folder_path)
            video_file_path = os.path.join(video_folder_path, "%s.mp4" % datetime.datetime.now().strftime("%Y%m%d%H%M%S%f"))
            with open(video_file_path, "wb") as f:
                f.write(base64.b64decode(video))
            self.log.info("video captured")

            if self.video_config["only_record_failed"]:
                stat_file = os.path.join(os.getcwd(), "projects", LoadConfig.load_config("project"), "test_reports", "stat.json")
                with open(stat_file, "r") as f:
                    current_stat = json.load(f)
                current_test = os.environ.get('PYTEST_CURRENT_TEST').split('::')
                current_test_file = current_test[0].split(os.sep)[-1].split(".")[0]
                current_test_name = current_test[-1].split(" ")[0]
                if current_stat["Details"][current_test_file][current_test_name].lower() == "pass":
                    os.remove(video_file_path)
                    self.log.info("remove video because current test pass")

    @classmethod
    def teardown_class(cls):
        super().teardown_class()
        AppiumHelper.close_driver()
        device = LoadConfig.load_config()["device"]
        if device.lower() == "stf":
            os.system("adb disconnect " + cls.remote_connect_url)
            cls.log.info(cls.remote_device.return_rented_device(cls.device_serial).text)

    @classmethod
    def start_app(cls):
        mobile = LoadConfig.load_config()["mobile"]
        device = LoadConfig.load_config()["device"]
        project = LoadConfig.load_config()["project"]
        if device.lower() == "stf":
            cls.remote_device = StfDevices(LoadConfig.load_config()["env"]["stf_host"])
            cls.device_serial = cls.remote_device.get_single_device()["serial"]
            cls.log.info("device serial: %s" % str(cls.device_serial))
            cls.log.info(cls.remote_device.rent_single_device(cls.device_serial).text)
            cls.remote_connect_url = cls.remote_device.get_user_device_remote_connect_url(cls.device_serial)
            cls.log.info("connect url: %s" % str(cls.remote_connect_url))
            os.system("adb connect " + cls.remote_connect_url)
            stf_caps = YamlHelper.load_yaml(os.path.join(os.getcwd(), "projects", project, "conf", "device_caps.yaml"))["STF"]
            device_cap = None
            for device in stf_caps.values():
                if device["deviceName"] == cls.device_serial:
                    device_cap = device
                    break
            cls._driver = AppiumHelper.get_driver(mobile, device_cap)
        else:
            device_cap = YamlHelper.load_yaml(os.path.join(os.getcwd(), "projects", project, "conf", "device_caps.yaml"))[device]
            cls._driver = AppiumHelper.get_driver(mobile, device_cap)

    @classmethod
    def restart_app(cls):
        AppiumHelper.close_driver()
        cls.start_app()
