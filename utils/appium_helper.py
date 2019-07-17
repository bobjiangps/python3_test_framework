from common.singleton import Singleton
from appium import webdriver


class AppiumHelper(Singleton):

    _driver = None

    @classmethod
    def get_current_driver(cls):
        return cls._driver

    @classmethod
    def get_driver(cls, mobile, device_caps):
        if cls._driver is None:
            driver_types = (AndroidDriver, IOSDriver)
            for driver_type in driver_types:
                if driver_type.name().lower() == mobile.lower():
                    cls._driver = driver_type.create(device_caps)
        return cls._driver

    @classmethod
    def close_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None


class AndroidDriver:

    @staticmethod
    def name():
        return "Android"

    @classmethod
    def create(cls, device_caps, port=4723):
        return webdriver.Remote('http://localhost:%s/wd/hub' % port, device_caps)


class IOSDriver:

    @staticmethod
    def name():
        return "iOS"

    @classmethod
    def create(cls, device_caps, port=4723):
        return webdriver.Remote('http://localhost:%s/wd/hub' % port, device_caps)
