from utils.selenium_helper import SeleniumHelper
from configuration.config import LoadConfig
from common.test_base.logged_test_case import LoggedTestCase
from selenium.common.exceptions import WebDriverException
from utils.video_helper import VideoHelper
import os
import json
import datetime


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
    def start_browser(cls):
        browser = LoadConfig.load_config()["browser"]
        if browser.lower() in ["chrome", "firefox", "ie", "edge", "safari"]:
            cls.log.info("Start to launch browser - %s" % browser)
            cls._driver = SeleniumHelper.get_driver(browser)
        else:
            device = LoadConfig.load_config()["device"]
            cls.log.info("Start to launch browser - %s with device name %s" % (browser, device))
            cls._driver = SeleniumHelper.get_driver(browser, device_name=device)
        try:
            if browser.lower() == "chrome":
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
        if "home_page" in LoadConfig.load_config()["env"].keys():
            home_page = LoadConfig.load_config()["env"]["home_page"]
            self.log.info(f"Go to home page: {home_page}")
            self.browse_page(home_page)
        else:
            self.log.info("no home page value, stay current page")
