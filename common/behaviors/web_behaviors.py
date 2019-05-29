from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class WebBehaviors(WebDriverWait):

    def __init__(self, driver, timeout, logger):
        super().__init__(driver, timeout)
        self.log = logger

    def format_locator(self, locator, *args):
        web_locators = list(By.__dict__.items())
        web_locators.extend([("IMAGE", "image")])
        by = value = None
        for k, v in web_locators:
            if v == locator["by"]:
                by = v
                value = locator["value"].format(*args)
                break
        self.log.info("by: %s, value: %s" % (by, value))
        return by, value

    def find_element(self, locator, *args):
        by, value = self.format_locator(locator, *args)
        try:
            return self._driver.find_element(by, value)
        except NoSuchElementException:
            raise NoSuchElementException("Unable to locate the element '{0}' through the {1} '{2}' in the page {3}".format(locator['locator_name'], by, value, self._driver.current_url))

    def find_elements(self, locator, *args):
        by, value = self.format_locator(locator, *args)
        return self._driver.find_elements(by, value)

    def open_new_window(self, url):
        self._driver.execute_script("window.open('%s')" % url)

    def close_all_windows(self):
        for window in self._driver.window_handles:
            self._driver.switch_to.window(window)
            self._driver.close()

    def switch_to_the_other_window(self):
        self._driver.switch_to_window(self._driver.window_handles[-1])

    def close_current_window(self):
        self._driver.close()
        self._driver.switch_to_window(self._driver.window_handles[-1])
