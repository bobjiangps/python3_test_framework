from common.test_base.page_base import PageBase


class CommonComponent(PageBase):

    def search_posts(self, text):
        self.log.info("Start to search posts with keyword: %s" % text)
        self.element("search_input").clear_then_input_value(text)
        self.element("search_button").click()
        self.element("search_button").wait_clickable()
        self.log.info("Complete to search posts with keyword: %s" % text)

    def go_to_login_page(self):
        self.log.info("Go to login page")
        self.element("login_link").click()

    def logout(self):
        self.log.info("Start to logout")
        self.element("logout_link").click()
        self.element("login_link").wait_visible()
        self.log.info("Complete to logout")
