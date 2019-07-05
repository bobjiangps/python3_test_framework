from common.behaviors.web_behaviors import WebBehaviors
from configuration.config import LoadConfig
from utils.yaml_helper import YamlHelper
from common.elements.button import Button
from common.elements.checkbox import Checkbox
from common.elements.dropdown import Dropdown
from common.elements.frame import Frame
from common.elements.input import Input
from common.elements.link import Link
from common.elements.radiobutton import RadioButton
from common.elements.static import Static
import os


class PageBase:

    def __init__(self, driver, logger):
        self._driver = driver
        self.log = logger
        self._config = LoadConfig.load_config()
        self.behavior = self.__init_behavior_by_project_type()
        element_file = os.path.join(os.getcwd(), "projects", self._config["project"], "pages", "elements", "%s.yaml" % self.__module__.split(".")[-1])
        if os.path.exists(element_file):
            self._elements = YamlHelper.load_yaml(element_file)
        else:
            self.log.critical("no element definition file found!!: %s" % element_file)

    def element_info(self, name):
        return self._elements[name]

    def element(self, name, *args):
        options = {
            "button": Button(self.behavior, self._elements[name], *args),
            "checkbox": Checkbox(self.behavior, self._elements[name], *args),
            "dropdown": Dropdown(self.behavior, self._elements[name], *args),
            "input": Input(self.behavior, self._elements[name], *args),
            "link": Link(self.behavior, self._elements[name], *args),
            "radiobutton": RadioButton(self.behavior, self._elements[name], *args),
            "text": Static(self.behavior, self._elements[name], *args),
            "pic": Static(self.behavior, self._elements[name], *args),
            "area": Static(self.behavior, self._elements[name], *args)
        }
        if self._elements[name]["type"].lower():
            return options[self._elements[name]["type"].lower()]
        else:
            self.log.info("%s is not a valid element type..." % self._elements[name]["type"])

    def frame(self, name, *args):
        if self._elements[name]["type"].lower().find("frame") >= 0:
            return Frame(self.behavior, self._elements[name], *args)
        else:
            self.log.info("%s is not a frame..." % self._elements[name]["value"])

    def __init_behavior_by_project_type(self):
        if self._config["report"]["ui_test"]:
            if self._config["report"]["app_test"]:
                return "todo, mobile"
            elif self._config["report"]["win_test"]:
                return "todo, windowssoftware"
            else:
                return WebBehaviors(self._driver, self._config["webdriver"]["timeout"], self.log)

    def current_url_contains(self, keyword):
        self.log.info("Check the current url contains: %s" % keyword)
        url = self.behavior.get_current_url()
        assert keyword in url, "current url is: %s doesn't contain: %s" % (url, keyword)

    def current_url(self):
        return self.behavior.get_current_url()
