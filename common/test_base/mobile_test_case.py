from utils.appium_helper import AppiumHelper
from utils.yaml_helper import YamlHelper
from utils.stf_helper import StfDevices
from configuration.config import LoadConfig
from common.test_base.logged_test_case import LoggedTestCase
import os


class MobileTestCase(LoggedTestCase):
    """Test case for testing web application"""

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.start_app()

    @classmethod
    def teardown_class(cls):
        super().teardown_class()
        device = LoadConfig.load_config()["device"]
        if device.lower() == "stf":
            os.system("adb disconnect " + cls.remote_connect_url)
            cls.log.info(cls.remote_device.return_rented_device(cls.device_serial).text)
        AppiumHelper.close_driver()

    @classmethod
    def start_app(cls):
        mobile = LoadConfig.load_config()["mobile"]
        device = LoadConfig.load_config()["device"]
        project = LoadConfig.load_config()["project"]
        if device.lower() == "stf":
            cls.remote_device = StfDevices(LoadConfig.load_config()["env"]["stf_host"])
            cls.device_serial = cls.remote_device.get_single_device()["serial"]
            cls.remote_connect_url = cls.remote_device.get_user_device_remote_connect_url(cls.device_serial)
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
