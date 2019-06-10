import copy


class ElementBase:

    def __init__(self, behavior, locator, *args):
        self._behavior = behavior
        temp_locator = copy.deepcopy(locator)
        temp_locator["value"] = temp_locator["value"].format(*args)
        self.locator = temp_locator

    def wait_presence(self):
        self._behavior.wait_until_presence_of_element(self.locator)

    def wait_visible(self):
        self._behavior.wait_until_visibility_of_element(self.locator)

    def wait_not_visible(self):
        self._behavior.wait_until_invisibility_of_element(self.locator)

    def wait_clickable(self):
        self._behavior.wait_until_element_to_be_clickable(self.locator)

    def element_selected(self):
        return self._behavior.element_selected(self.locator)

    def element_enabled(self):
        return self._behavior.element_enabled(self.locator)

    def element_displayed(self):
        return self._behavior.element_displayed(self.locator)

    def element_exist(self):
        return self._behavior.element_exist(self.locator)

    def get_element_property(self, property_name):
        return self._behavior.get_element_property(property_name, self.locator)

    def get_element_text(self):
        return self._behavior.get_element_text(self.locator)

    def get_element_attribute(self, attribute_name):
        return self._behavior.get_element_attribute(attribute_name, self.locator)

    def check_property(self, expect, property_name):
        actual = self.get_element_property(property_name)
        assert expect == actual, "Check property fail, expect value is: %s, but actual value is: %s" % (expect, actual)

    def check_attribute(self, expect, attribute_name):
        actual = self.get_element_attribute(attribute_name)
        assert expect == actual, "Check attribute fail, expect value is: %s, but actual value is: %s" % (expect, actual)

    def check_text(self, expect):
        actual = self.get_element_text()
        assert expect == actual, "Check text fail, expect value is: %s, but actual value is: %s" % (expect, actual)

    def all(self):
        return self._behavior.find_elements(self.locator)

    def count(self):
        return len(self.all())
