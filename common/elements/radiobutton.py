from common.elements.element_base import ElementBase


class RadioButton(ElementBase):

    def select(self):
        if not self.element_selected():
            self._behavior.click(self.locator)

    def deselect(self):
        if self.element_selected():
            self._behavior.click(self.locator)
