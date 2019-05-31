from common.test_base.web_test_case import WebTestCase
from projects.byblog.pages.home_page import HomePage


class BlogWebTestCase(WebTestCase):
    """Test case for testing by blog"""

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.home_page = HomePage(cls._driver, cls.log)
