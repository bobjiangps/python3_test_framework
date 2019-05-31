from common.test_base.page_base import PageBase


class CommonComponent(PageBase):

    def search_posts(self, text):
        self.log.info("Start to search posts with keyword: %s" % text)
        result = self.behavior.find_element(self.element("search_input"))
        self.log.info(result)
        #todo
        self.log.info("End to search posts with keyword: %s" % text)
