from common.test_base.web_test_case import WebTestCase
from ..pages.main_page import MainPage
from ..pages.post_list_page import PostListPage
from ..pages.login_page import LoginPage
from ..pages.post_detail_page import PostDetailPage


class BlogWebTestCase(WebTestCase):
    """Test case for testing by blog"""

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.main_page = MainPage(cls._driver, cls.log)
        cls.post_list_page = PostListPage(cls._driver, cls.log)
        cls.login_page = LoginPage(cls._driver, cls.log)
        cls.post_detail_page = PostDetailPage(cls._driver, cls.log)
