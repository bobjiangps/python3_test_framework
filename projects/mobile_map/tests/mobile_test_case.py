from common.test_base.mobile_test_case import MobileTestCase
from projects.mobile_map.pages.main_page import MainPage
from projects.mobile_map.pages.route_page import RoutePage
from projects.mobile_map.pages.personal_page import PersonalPage


class MapMobileTestCase(MobileTestCase):
    """Test case for testing map"""

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.main_page = MainPage(cls._driver, cls.log)
        cls.route_page = RoutePage(cls._driver, cls.log)
        cls.personal_page = PersonalPage(cls._driver, cls.log)
