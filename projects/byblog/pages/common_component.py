from common.test_base.page_base import PageBase
from utils.mysql_helper import MysqlConnection


class CommonComponent(PageBase):

    def search_posts(self, text):
        self.log.info("Start to search posts with keyword: %s" % text)
        self.element("search_input").clear_then_input_value(text)
        self.element("search_button").click()
        self.behavior.wait_page_load()
        self.element("search_button").wait_clickable()
        self.log.info("Complete to search posts with keyword: %s" % text)

    def go_to_login_page(self):
        self.log.info("Go to login page")
        self.element("login_link").click()

    def go_to_post_list_page(self):
        self.log.info("Go to post list page")
        self.element("post_list_link").click()

    def logout(self):
        self.log.info("Start to logout")
        self.element("logout_link").click()
        self.element("login_link").wait_visible()
        self.log.info("Complete to logout")

    def get_id_title_of_random_post(self):
        self.log.info("Query in database to get id and title of random post")
        db = MysqlConnection().connect("test_db")
        sql = "select id, title from blog_post where visiable_id=1;"
        result = db.get_random_result_from_database(sql)
        self.log.info(f"the query result is: {result}")
        return result
