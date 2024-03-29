from common.behaviors.web_behaviors import WebBehaviors
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from configuration.config import LoadConfig
from utils.cv_helper import CVHelper
import os
import time


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

    def click(self, locator, *args):
        by, value = self.format_locator(locator, *args)
        self.log.info("Click the element found by %s: %s" % (by, value))
        if by != "image":
            try:
                element = self.wait_until_element_to_be_clickable(locator, *args)
            except:
                element = self.find_element(locator, *args)
            element.click()
        else:
            test_data_path = os.path.join(os.getcwd(), "projects", LoadConfig.load_config()["project"], "test_data")
            screenshot_path = os.path.join(test_data_path, "screenshot.png")
            element_img_path = os.path.join(test_data_path, value)
            self._driver.save_screenshot(screenshot_path)
            time.sleep(1)
            if os.path.exists(screenshot_path):
                scale_x, scale_y = CVHelper.flann_generate_matched_points_center(element_img_path, screenshot_path)
                window_size = self._driver.get_window_size()
                x = round(scale_x * window_size["width"], 2)
                y = round(scale_y * window_size["height"], 2)
                self.log.info(f"click on the coordinates: {x}, {y}")
                self._driver.tap([(x, y)])
            else:
                self.log.info("unable to find the screenshot file")

    def swipe(self, direction, duration=1000):
        self.log.info("Swipe to direction: %s" % direction)
        if LoadConfig.load_config()["device"].lower().startswith("ip"):
            self._driver.execute_script("mobile: swipe", {"direction": direction})
        else:
            screen_size = self._driver.get_window_size()
            directions = {
                "up": {"start_x": screen_size.width / 2, "start_y": screen_size.height * 3 / 4, "end_x": screen_size.width / 2, "end_y": screen_size.height / 4, duration: duration},
                "down": {"start_x": screen_size.width / 2, "start_y": screen_size.height / 4, "end_x": screen_size.width / 2, "end_y": screen_size.height * 3 / 4, duration: duration},
                "left": {"start_x": screen_size.width * 4 / 5, "start_y": screen_size.height / 2, "end_x": screen_size.width / 5, "end_y": screen_size.height / 2, duration: duration},
                "right": {"start_x": screen_size.width / 5, "start_y": screen_size.height / 2, "end_x": screen_size.width * 4 / 5, "end_y": screen_size.height / 2, duration: duration}
            }
            self._driver.swipe(directions[direction]["start_x"], directions[direction]["start_y"], directions[direction]["end_x"], directions[direction]["end_y"], duration)

    def tap(self, locator, *args):
        element = self.wait_until_visibility_of_element(locator, *args)
        self.log.info("Tap the element")
        TouchAction(self._driver).tap(element).perform()

    def tap_on_coordinates(self, x, y, duration=500):
        self._driver.tap([(x, y)], duration)

    def switch_to_context(self, context):
        return self._driver.switch_to.context(context)

    def get_current_context(self):
        return self._driver.current_context

    def get_all_contexts(self):
        return self._driver.contexts

    def get_current_orientation(self):
        return self._driver.orientation()

    def rotate(self, orientation):
        self.log.info(f"Change orientation to {orientation}")
        options = ["LANDSCAPE", "PORTRAIT"]
        if orientation in options:
            if orientation.lower() == self.get_current_orientation().lower():
                self.log.info(f"Already in {orientation}, no need to rotate")
            else:
                self._driver.orientation = orientation
        else:
            raise WebDriverException("You can only set the orientation to 'LANDSCAPE' or 'PORTRAIT'.")
