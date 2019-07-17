from utils.appium_helper import AppiumHelper
from utils.yaml_helper import YamlHelper
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
        AppiumHelper.close_driver()

    @classmethod
    def start_app(cls):
        mobile = LoadConfig.load_config()["mobile"]
        device = LoadConfig.load_config()["device"]
        project = LoadConfig.load_config()["project"]
        device_cap = YamlHelper.load_yaml(os.path.join(os.getcwd(), "projects", project, "conf", "device_caps.yaml"))[device]
        cls._driver = AppiumHelper.get_driver(mobile, device_cap)

    @classmethod
    def restart_app(cls):
        AppiumHelper.close_driver()
        cls.start_app()
