from projects.mobile_stf.tests.mobile_test_case import STFMobileTestCase


class TestSTF(STFMobileTestCase):
    """test with stf devices, auto assign"""

    def test_calculator_with_stf_devices(self):
        """test calculator with stf devices"""
        with self.verify():
            self.calculate_page.add_function_should_works_when_add_single_digit()
