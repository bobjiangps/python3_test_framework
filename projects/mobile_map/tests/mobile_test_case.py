from common.test_base.mobile_test_case import MobileTestCase
from ..pages.main_page import MainPage
from ..pages.route_page import RoutePage
from ..pages.personal_page import PersonalPage


class MapMobileTestCase(MobileTestCase):
    """Test case for testing map"""

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.main_page = MainPage(cls._driver, cls.log)
        cls.route_page = RoutePage(cls._driver, cls.log)
        cls.personal_page = PersonalPage(cls._driver, cls.log)
