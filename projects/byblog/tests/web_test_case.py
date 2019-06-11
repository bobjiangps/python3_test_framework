from common.test_base.web_test_case import WebTestCase
from projects.byblog.pages.post_list_page import PostListPage
from projects.byblog.pages.login_page import LoginPage


class BlogWebTestCase(WebTestCase):
    """Test case for testing by blog"""

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.post_list_page = PostListPage(cls._driver, cls.log)
        cls.login_page = LoginPage(cls._driver, cls.log)
