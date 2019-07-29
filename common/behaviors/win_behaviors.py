from pywinauto import findwindows, mouse
from utils.cv_helper import CVHelper
from utils.win32_helper import Win32Helper
from configuration.config import LoadConfig
import time
import os


class WinBehaviors:

    def __init__(self, driver, timeout, logger):
        self._driver = driver
        self.log = logger
        self.timeout = timeout
        self._window = None

    def format_locator(self, locator, *args):
        win_by = ["text", "title", "title_re", "class_name", "class_name_re", "name", "image"]
        for v in win_by:
            if v == locator["by"]:
                by = v
                value = locator["value"].format(*args)
                break
        return by, value

    def find_element(self, locator, *args):
        self._window = self.find_window(locator["window"])
        self._window.wait("visible", timeout=self.timeout)
        by, value = self.format_locator(locator, *args)
        return self._window[value]

    def find_elements(self, locator, *args):
        by, value = self.format_locator(locator, *args)
        if by == "title":
            return findwindows.find_elements(title=value)
        elif by == "title_re":
            return findwindows.find_elements(title_re=value)
        elif by == "class_name":
            return findwindows.find_elements(class_name=value)
        elif by == "class_name_re":
            return findwindows.find_elements(class_name_re=value)
        else:
            self.log.warning("%s is not support when find elements" % by)

    def find_window(self, locator, *args):
        by, value = self.format_locator(locator, *args)
        if by == "title":
            return self._driver.window(title=value)
        elif by == "title_re":
            return self._driver.window(title_re=value)
        elif by == "class_name":
            return self._driver.window(class_name=value)
        elif by == "class_name_re":
            return self._driver.window(class_name_re=value)
        else:
            self.log.warning("%s is not support when find window" % by)

    def find_windows(self, locator, *args):
        by, value = self.format_locator(locator, *args)
        if by == "title":
            return self._driver.windows(title=value)
        elif by == "title_re":
            return self._driver.windows(title_re=value)
        elif by == "class_name":
            return self._driver.windows(class_name=value)
        elif by == "class_name_re":
            return self._driver.windows(class_name_re=value)
        else:
            self.log.warning("%s is not support when find windows" % by)

    def get_top_window(self):
        return self._driver.top_window()

    def select_menu(self, window_locator, menu_list):
        self._window = self.find_window(window_locator)
        self._window.menu_select("->".join(menu_list))

    def wait_until_presence_of_element(self, locator, *args):
        by, value = self.format_locator(locator, *args)
        message = "Unable to find the element by {0}: '{1}'".format(by, value)
        element = self.find_element(locator, *args)
        try:
            element.wait("exists", timeout=self.timeout)
            return element
        except:
            self.log.critical(message)
            return False

    def wait_until_element_disappear(self, locator, *args):
        by, value = self.format_locator(locator, *args)
        message = "Still find the element by {0}: '{1}'".format(by, value)
        element = self.find_element(locator, *args)
        try:
            element.wait_not("exists", timeout=self.timeout)
            return True
        except:
            self.log.critical(message)
            return False

    def wait_until_invisibility_of_element(self, locator, *args):
        by, value = self.format_locator(locator, *args)
        message = "The element by {0}: '{1}' is still visible".format(by, value)
        element = self.find_element(locator, *args)
        try:
            element.wait_not("visible", timeout=self.timeout)
            return True
        except:
            self.log.critical(message)
            return False

    def wait_until_visibility_of_element(self, locator, *args):
        by, value = self.format_locator(locator, *args)
        message = "The element by {0}: '{1}' is not visible".format(by, value)
        element = self.find_element(locator, *args)
        try:
            element.wait("visible", timeout=self.timeout)
            return element
        except:
            self.log.critical(message)
            return False

    def wait_until_element_to_be_clickable(self, locator, *args):
        by, value = self.format_locator(locator, *args)
        message = "The element by {0}: '{1}' is not clickable".format(by, value)
        element = self.find_element(locator, *args)
        try:
            element.wait("ready", timeout=self.timeout)
            return element
        except:
            self.log.critical(message)
            return False

    def click(self, locator, *args):
        by, value = self.format_locator(locator, *args)
        self.log.info("Click the element found by %s: %s" % (by, value))
        if by != "image":
            element = self.wait_until_element_to_be_clickable(locator, *args)
            element.click()
        else:
            test_data_path = os.path.join(os.getcwd(), "projects", LoadConfig.load_config()["project"], "test_data")
            screenshot_path = os.path.join(test_data_path, "screenshot.png")
            element_img_path = os.path.join(test_data_path, value)
            width, height = Win32Helper.capture_screen(screenshot_path)
            time.sleep(1)
            if os.path.exists(screenshot_path):
                scale_x, scale_y = CVHelper.flann_generate_matched_points_center(element_img_path, screenshot_path)
                x = round(scale_x * width, 2)
                y = round(scale_y * height, 2)
                self.log.info(f"click on the coordinates: {x}, {y}")
                Mouse.click("left", (x, y))
            else:
                self.log.info("unable to find the screenshot file")

    def clear(self, locator, *args):
        by, value = self.format_locator(locator, *args)
        self.log.info("Clear the element found by %s: %s" % (by, value))
        element = self.find_element(locator, *args)
        element.set_text("")

    def send_keys(self, keys_value, locator, *args):
        by, value = self.format_locator(locator, *args)
        self.log.info("Send keys(%s) to the element found by %s: %s" % (keys_value, by, value))
        element = self.find_element(locator, *args)
        element.type_keys(keys_value, with_spaces=True)

    def clear_and_send_keys(self, keys_value, locator, *args):
        by, value = self.format_locator(locator, *args)
        self.log.info("Clear and send keys(%s) to the element found by %s: %s" % (keys_value, by, value))
        element = self.find_element(locator, *args)
        element.set_text(keys_value)

    def select_by_text(self, select_text, locator, *args):
        by, value = self.format_locator(locator, *args)
        self.log.info("Select the text(%s) from the element found by %s: %s" % (select_text, by, value))
        element = self.find_element(locator, *args)
        element.select(select_text)

    def select_by_value(self, select_value, locator, *args):
        self.select_by_text(select_value, locator, *args)

    def select_by_index(self, index, locator, *args):
        by, value = self.format_locator(locator, *args)
        self.log.info("Select the index(%s) from the element found by %s: %s" % (index, by, value))
        element = self.find_element(locator, *args)
        element.select(index)

    def first_selected_option(self, locator, *args):
        by, value = self.format_locator(locator, *args)
        self.log.info("Get the first selected option from the element found by %s: %s" % (by, value))
        element = self.find_element(locator, *args)
        return element.selected_text()

    def element_selected(self, locator, *args):
        element = self.wait_until_visibility_of_element(locator, *args)
        if element.is_editable():
            self.log.info("The element is already selected")
        else:
            self.log.info("The element is not selected")
        return element.is_editable()

    def element_enabled(self, locator, *args):
        element = self.find_element(locator, *args)
        try:
            element.wait("enabled", timeout=self.timeout)
            return True
        except:
            return False

    def element_displayed(self, locator, *args):
        element = self.find_element(locator, *args)
        try:
            element.wait("visible", timeout=self.timeout)
            return True
        except:
            return False

    def element_exist(self, locator, *args):
        element = self.find_element(locator, *args)
        return element.exists()

    def get_element_text(self, locator, *args):
        element = self.wait_until_visibility_of_element(locator, *args)
        return element.texts
