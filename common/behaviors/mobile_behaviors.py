from common.behaviors.web_behaviors import WebBehaviors
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


class MobileBehaviors(WebBehaviors):

    def format_locator(self, locator, *args):
        mobile_locators = list(MobileBy.__dict__.items())
        default_locators = list(By.__dict__.items())
        mobile_locators.extend(default_locators)
        mobile_locators.extend([("IMAGE", "image")])
        by = value = None
        for k, v in mobile_locators:
            if v == locator["by"]:
                by = v
                value = locator["value"].format(*args)
                break
        return by, value

    def swipe(self):
        pass

    def tap(self):
        pass

    def switch_to_context(self):
        pass

    def get_current_context(self):
        pass

    def get_all_contexts(self):
        pass
