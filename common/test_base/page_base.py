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
        self.behavior = WebBehaviors(self._driver, self._config["webdriver"]["timeout"], self.log)
        element_file = os.path.join(os.getcwd(), "projects", self._config["project"], "pages", "elements", "%s.yaml" % self.__module__.split(".")[-1])
        if os.path.exists(element_file):
            self.elements = YamlHelper.load_yaml(element_file)
        else:
            self.log.critical("no element definition file found!!: %s" % element_file)

    def element_info(self, name):
        return self.elements[name]

    def element(self, name, *args):
        options = {
            "button": Button(self.behavior, self.elements[name], *args),
            "checkbox": Checkbox(self.behavior, self.elements[name], *args),
            "dropdown": Dropdown(self.behavior, self.elements[name], *args),
            "input": Input(self.behavior, self.elements[name], *args),
            "link": Link(self.behavior, self.elements[name], *args),
            "radiobutton": RadioButton(self.behavior, self.elements[name], *args),
            "text": Static(self.behavior, self.elements[name], *args)
        }
        if self.elements[name]["type"].lower():
            return options[self.elements[name]["type"].lower()]
        else:
            self.log.info("%s is not a valid element type..." % self.elements[name]["type"])

    def frame(self, name, *args):
        if self.elements[name]["type"].lower().find("frame") >= 0:
            return Frame(self.behavior, self.elements[name], *args)
        else:
            self.log.info("%s is not a frame..." % self.elements[name]["value"])
