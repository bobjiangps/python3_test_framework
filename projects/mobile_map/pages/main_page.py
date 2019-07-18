from common.test_base.page_base import PageBase


class MainPage(PageBase):

    def start_route(self):
        self.log.info("Start to route")
        self.element("start_route_button").click()
