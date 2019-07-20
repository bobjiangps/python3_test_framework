from common.test_base.mobile_test_case import MobileTestCase
from projects.mobile_stf.pages.calculate_page import CalculatePage


class STFMobileTestCase(MobileTestCase):
    """Test case for testing stf"""

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.calculate_page = CalculatePage(cls._driver, cls.log)
