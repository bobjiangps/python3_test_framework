from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from common.singleton import Singleton
from selenium import webdriver


class SeleniumHelper(Singleton):

    _driver = None

    @classmethod
    def get_current_driver(cls):
        return cls._driver

    @classmethod
    def get_driver(cls, browser, caps=None):
        if cls._driver is None:
            driver_types = (ChromeDriver, FirefoxDriver, IEDriver, EdgeDriver, SafariDriver)
            for driver_type in driver_types:
                if driver_type.name().lower() == browser.lower():
                    cls._driver = driver_type.create(caps)
        return cls._driver

    @classmethod
    def close_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None


class ChromeDriver:

    @classmethod
    def name(cls):
        return "Chrome"

    @classmethod
    def create(cls, caps):
        if caps:
            return webdriver.Chrome(desired_capabilities=caps)
        else:
            return webdriver.Chrome()


class FirefoxDriver:

    @classmethod
    def name(cls):
        return "Firefox"

    @classmethod
    def create(cls, caps):
        if caps:
            return webdriver.Firefox(desired_capabilities=caps)
        else:
            return webdriver.Firefox()


class IEDriver:

    @classmethod
    def name(cls):
        return "IE"

    @classmethod
    def create(cls, caps):
        if caps:
            return webdriver.Ie(desired_capabilities=caps)
        else:
            return webdriver.Ie()


class EdgeDriver:

    @classmethod
    def name(cls):
        return "Edge"

    @classmethod
    def create(cls, caps):
        if caps:
            return webdriver.Edge(desired_capabilities=caps)
        else:
            return webdriver.Edge()


class SafariDriver:

    @classmethod
    def name(cls):
        return "Safari"

    @classmethod
    def create(cls, caps):
        if caps:
            return webdriver.Safari(desired_capabilities=caps)
        else:
            return webdriver.Safari()
