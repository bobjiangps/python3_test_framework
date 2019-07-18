from common.elements.element_base import ElementBase


class Input(ElementBase):

    def clear(self):
        self._behavior.clear(self.locator)

    def input_value(self, value):
        self._behavior.send_keys(value, self.locator)

    def clear_then_input_value(self, value):
        self._behavior.clear_and_send_keys(value, self.locator)

    def click(self):
        self._behavior.click(self.locator)
