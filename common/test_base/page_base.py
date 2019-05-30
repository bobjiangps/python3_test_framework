from common.behaviors.web_behaviors import WebBehaviors
from configuration.config import LoadConfig
from utils.yaml_helper import YamlHelper
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

    def element(self, name):
        return self.elements[name]
