import pytest
from configuration.config import LoadConfig


class TestSample:

    def test_answer1(self):
        """this is description of test answer1"""
        assert 2+3 == 5

    @pytest.mark.error
    def test_answer2(self):
        """this is description of test answer2"""
        assert 2 + 4 == 5

    @pytest.mark.sample
    @pytest.mark.temp
    def test_answer3(self):
        """this is description of test answer3"""
        assert 2+3 == 5

    @pytest.mark.skipif(LoadConfig.load_config()["tag"].lower() in ["staging", "prod", "all"], reason="not ready")
    def test_answer4(self):
        """this is description of test answer4"""
        assert 2 + 4 == 5
