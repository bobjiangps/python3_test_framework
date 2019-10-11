import pytest
from configuration.config import LoadConfig
from common.test_base.logged_test_case import LoggedTestCase


class TestSample(LoggedTestCase):

    def test_answer1(self):
        """TEMP-1: this is description of test answer1"""
        assert 2+3 == 5

    @pytest.mark.error
    def test_answer2(self):
        """TEMP-2: this is description of test answer2"""
        assert 2 + 4 == 5

    @pytest.mark.sample
    @pytest.mark.temp
    def test_answer3(self):
        """TEMP-3: this is description of test answer3"""
        assert 2+3 == 5

    @pytest.mark.skipif(LoadConfig.load_config()["tag"].lower() in ["staging", "prod", "all"], reason="not ready")
    def test_answer4(self):
        """TEMP-4: this is description of test answer4"""
        assert 2 + 4 == 5
