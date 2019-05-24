from utils.selenium_helper import SeleniumHelper
from configuration.config import LoadConfig
from common.test_base.logged_test_case import LoggedTestCase
from selenium.common.exceptions import WebDriverException


class WebTestCase(LoggedTestCase):
    """Test case for testing web application"""

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.start_browser()

    @classmethod
    def teardown_class(cls):
        super().teardown_class()
        SeleniumHelper.close_driver()

    def setup_method(self):
        super().setup_method()
        self.browser_home_page()

    @classmethod
    def start_browser(cls):
        cls.log.info("Start to launch browser - %s" % LoadConfig.load_config()["browser"])
        cls._driver = SeleniumHelper.get_driver(LoadConfig.load_config()["browser"])
        try:
            if LoadConfig.load_config()["browser"].lower() == "chrome":
                width, height = cls._driver.execute_script("return [window.screen.availWidth, window.screen.availHeight];")
                cls.log.info(f"set window size to width: {width} and height: {height}")
                cls._driver.set_window_size(width, height)
            else:
                cls.log.info("maximize browser window")
                cls._driver.maximize_window()
        except WebDriverException as e:
            cls.log.warning("fail to set window size: %s" % str(e))

    @classmethod
    def restart_browser(cls):
        SeleniumHelper.close_driver()
        cls.start_browser()

    def browse_page(self, page_url):
        self.log.info("Browse page %s" % page_url)
        self._driver.get(page_url)

    def browser_home_page(self):
        env_name = LoadConfig.load_config()["environment"]
        if "home_page" in LoadConfig.load_config()["env"][env_name].keys():
            home_page = LoadConfig.load_config()["env"][env_name]["home_page"]
            self.log.info(f"Go to home page: {home_page}")
            self.browse_page(home_page)
        else:
            self.log.info("no home page value, stay current page")
