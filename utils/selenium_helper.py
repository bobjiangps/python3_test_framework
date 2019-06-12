from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from common.singleton import Singleton
from selenium import webdriver


class SeleniumHelper(Singleton):

    _driver = None

    @classmethod
    def get_current_driver(cls):
        return cls._driver

    @classmethod
    def get_driver(cls, browser, caps=None, device_name=None):
        if cls._driver is None:
            driver_types = (ChromeDriver, FirefoxDriver, IEDriver, EdgeDriver, SafariDriver, SimulateMobileBrowserDriver)
            for driver_type in driver_types:
                if driver_type.name().lower() == browser.lower():
                    if SimulateMobileBrowserDriver.name().lower() == browser.lower():
                        cls._driver = driver_type.create(device_name)
                    else:
                        cls._driver = driver_type.create(caps)
        return cls._driver

    @classmethod
    def close_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None


class ChromeDriver:

    @staticmethod
    def name():
        return "Chrome"

    @classmethod
    def create(cls, caps):
        if caps:
            return webdriver.Chrome(desired_capabilities=caps)
        else:
            return webdriver.Chrome()


class FirefoxDriver:

    @staticmethod
    def name():
        return "Firefox"

    @classmethod
    def create(cls, caps):
        if caps:
            return webdriver.Firefox(desired_capabilities=caps)
        else:
            return webdriver.Firefox()


class IEDriver:

    @staticmethod
    def name():
        return "IE"

    @classmethod
    def create(cls, caps):
        if caps:
            return webdriver.Ie(desired_capabilities=caps)
        else:
            return webdriver.Ie()


class EdgeDriver:

    @staticmethod
    def name():
        return "Edge"

    @classmethod
    def create(cls, caps):
        if caps:
            return webdriver.Edge(desired_capabilities=caps)
        else:
            return webdriver.Edge()


class SafariDriver:

    @staticmethod
    def name():
        return "Safari"

    @classmethod
    def create(cls, caps):
        if caps:
            return webdriver.Safari(desired_capabilities=caps)
        else:
            return webdriver.Safari()


class SimulateMobileBrowserDriver:

    @staticmethod
    def name():
        return "MobileBrowser"

    @classmethod
    def create(cls, device_name):
        user_agents = {
            "iPhone": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1",
            "Android": "Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36",
            "iPad": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Mobile/15E148 Safari/604.1"
        }
        device_metrics = {
            "iPhone": {"width": 360, "height": 640},
            "Android": {"width": 360, "height": 640},
            "iPad": {"width": 768, "height": 1024},
        }
        if device_name in user_agents.keys():
            mobile_emulation = {"deviceMetrics": device_metrics[device_name], "userAgent": user_agents[device_name]}
            print(mobile_emulation)
        else:
            mobile_emulation = {"deviceName": device_name}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        return webdriver.Chrome(options=chrome_options)
