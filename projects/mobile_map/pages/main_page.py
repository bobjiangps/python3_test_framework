from common.test_base.page_base import PageBase


class MainPage(PageBase):

    def start_route(self):
        self.log.info("Start to route")
        self.element("start_route_button").click()

    def go_to_personal_page(self):
        self.log.info("user go to personal page")
        self.element("user_head_pic").click()
        # self.element("user_head_pic_img").click()
        self.element("user_level").wait_presence()
