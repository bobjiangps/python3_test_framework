from common.test_base.page_base import PageBase


class CommonComponent(PageBase):

    def search_posts(self, text):
        self.log.info("Start to search posts with keyword: %s" % text)
        self.element("search_input").clear_then_input_value(text)
        self.element("search_button").click()
        self.element("search_button").wait_clickable()
        self.log.info("End to search posts with keyword: %s" % text)
