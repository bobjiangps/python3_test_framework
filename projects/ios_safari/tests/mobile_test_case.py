from common.test_base.mobile_test_case import MobileTestCase
from projects.ios_safari.pages.main_page import MainPage
from projects.ios_safari.pages.post_list_page import PostListPage


class BlogMobileTestCase(MobileTestCase):
    """Test case for testing by blog"""

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.main_page = MainPage(cls._driver, cls.log)
        cls.post_list_page = PostListPage(cls._driver, cls.log)
