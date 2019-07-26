from common.singleton import Singleton
from pywinauto import Application


class WinautoHelper(Singleton):

    _driver = None

    @classmethod
    def get_current_driver(cls):
        return cls._driver

    @classmethod
    def get_driver(cls, executable, caps):
        default_caps = {"backend": "win32"}
        caps = dict(default_caps, **caps)
        cls._driver = WinDriver.create(executable, caps)
        return cls._driver

    @classmethod
    def close_driver(cls):
        if cls._driver is not None:
            cls._driver.kill(soft=True)
            cls._driver = None


class WinDriver:

    @classmethod
    def create(cls, executable, caps):
        return Application(backend=caps["backend"]).start(executable)
