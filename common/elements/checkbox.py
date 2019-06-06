from common.elements.element_base import ElementBase


class Checkbox(ElementBase):

    def check(self):
        if not self.element_selected():
            self._behavior.click(self.locator)

    def uncheck(self):
        if self.element_selected():
            self._behavior.click(self.locator)
