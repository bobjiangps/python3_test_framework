#from common.test_base.web_test_case import WebTestCase
from projects.byblog.tests.web_test_case import BlogWebTestCase


class TestViewPosts(BlogWebTestCase):

    def test_view_home_page(self):
        """user is able to view home page"""
        # self.browse_page("https://www.baidu.com")
        # self._driver.get("https://www.bing.com")
        # import time
        # time.sleep(3)
        # self.home_page.search_posts("webdriver")
        # time.sleep(2)
        # #assert False
        import time
        time.sleep(2)
        self.home_page.search_posts("webdriver")
        self.home_page.navigate_to_page_num(3)
