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
            raise NoSuchElementException("Unable to locate the element by {0}: '{1}' in the page {2}".format(by, value, self._driver.current_url))

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
        self._driver.switch_to.window(self._driver.window_handles[-1])

    def close_current_window(self):
        self._driver.close()
        self._driver.switch_to.window(self._driver.window_handles[-1])

    def wait_until_presence_of_element(self, locator, *args):
        by, value = self.format_locator(locator, *args)
        message = "Unable to find the element by {0}: '{1}' in the page '{2}'".format(by, value, self._driver.current_url)
        return self.until(EC.presence_of_element_located((by, value)), message)

    def wait_until_frame_to_be_available_and_switch_to_it(self, locator, *args):
        by, value = self.format_locator(locator, *args)
        message = "Unable to switch to the frame to be available by {0}: '{1}' in the page '{2}'".format(by, value, self._driver.current_url)
        el = self.until_visibility_of_element(locator, *args)
        return self.until(EC.frame_to_be_available_and_switch_to_it(el), message)

    def wait_until_switch_to_default_content(self):
        message = "Unable to switch to the default frame in the page '{0}'".format(self._driver.current_url)
        return self.until(EC.frame_to_be_available_and_switch_to_it(None), message)

    def wait_until_invisibility_of_element_located(self, locator, *args):
        by, value = self.format_locator(locator, *args)
        message = "Unable to get the element to be invisible by {0}: '{1}' in the page '{2}'".format(by, value, self._driver.current_url)
        return self.until(EC.invisibility_of_element_located((by, value)), message)

    def wait_until_visibility_of_element(self, locator, *args):
        by, value = self.format_locator(locator, *args)
        message = "Unable to get the element to be visible by {0}: '{1}' in the page '{2}'".format(by, value, self._driver.current_url)
        return self.until(EC.visibility_of_element_located((by, value)), message)

    def wait_until_element_to_be_clickable(self, locator, *args):
        by, value = self.format_locator(locator, *args)
        message = "Unable to get the element to be clickable by {0}: '{1}' in the page '{2}'".format(by, value, self._driver.current_url)
        return self.until(EC.element_to_be_clickable((by, value)), message)

    def wait_until_element_to_be_selected(self, locator, *args):
        by, value = self.format_locator(locator, *args)
        message = "Unable to get the element to be clickable by {0}: '{1}' in the page '{2}'".format(by, value, self._driver.current_url)
        return self.until(EC.element_to_be_selected((by, value)), message)

    def wait_until_text_to_be_present_in_element(self, locator, text, *args):
        by, value = self.format_locator(locator, *args)
        message = "Unable to get '{2}' to be present in the element by {0}: '{1}' in the page '{3}'".format(by, value, text, self._driver.current_url)
        return self.until(EC.text_to_be_present_in_element((by, value)), message)

    def wait_until_element_located_selection_state_to_be(self, locator, is_selected, *args):
        by, value = self.format_locator(locator, *args)
        message = "Unable to get the element to be located selection state by {0}: '{1}' in the page '{2}'".format(by, value, self._driver.current_url)
        return self.until(EC.element_located_selection_state_to_be((by, value), is_selected), message)

    def wait_until_alert_is_present(self):
        message = "Unable to get alert to be present in the page %s" % self._driver.current_url
        return self.until(EC.alert_is_present(), message)
