from common.elements.element_base import ElementBase


class Dropdown(ElementBase):

    def select_by_text(self, text):
        self._behavior.select_by_text(text, self.locator)

    def select_by_value(self, value):
        self._behavior.select_by_value(value, self.locator)

    def select_by_index(self, index):
        self._behavior.select_by_index(index, self.locator)
