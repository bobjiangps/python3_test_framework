from utils.winauto_helper import WinautoHelper
from utils.yaml_helper import YamlHelper
from configuration.config import LoadConfig
from common.test_base.logged_test_case import LoggedTestCase
import os


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
