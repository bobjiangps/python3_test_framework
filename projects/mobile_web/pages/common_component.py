from common.test_base.page_base import PageBase
from configuration.config import LoadConfig


class CommonComponent(PageBase):

    def search_posts(self, text):
        self.log.info("Start to search posts with keyword: %s" % text)
        self.element("search_input").clear_then_input_value(text)
        self.element("search_button").click()
        self.behavior.wait_page_load()
        self.element("search_button").wait_clickable()
        self.log.info("Complete to search posts with keyword: %s" % text)

    def go_to_home_page(self):
        home_page = LoadConfig.load_config()["env"]["home_page"]
        self.log.info(f"Go to home page: {home_page}")
        self.behavior.go_to_page(home_page)
        self.element("search_button").wait_clickable()
