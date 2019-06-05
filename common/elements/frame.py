from common.elements.element_base import ElementBase


class Frame(ElementBase):

    def switch_to_frame(self):
        self._behavior.wait_until_frame_to_be_available_and_switch_to_it(self.locator)

    def switch_to_default_content(self):
        self._behavior.wait_until_switch_to_default_content()
