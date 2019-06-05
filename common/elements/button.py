from common.elements.element_base import ElementBase


class Button(ElementBase):

    def click(self):
        self._behavior.click(self.locator)
