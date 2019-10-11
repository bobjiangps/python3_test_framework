import pytest
from common.test_base.logged_test_case import LoggedTestCase


class TestSample2(LoggedTestCase):

    def test_answer5(self):
        """TEMP-5: this is description of test answer5"""
        assert 2+3 == 5

    def test_answer6(self):
        """TEMP-6: this is description of test answer6"""
        assert 2 + 4 == 5

    @pytest.mark.temp
    def test_answer7(self):
        """TEMP-7: this is description of test answer7"""
        assert 2+3 == 5