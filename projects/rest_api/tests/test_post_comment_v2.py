from common.test_base.logged_test_case import LoggedTestCase
from common.test_base.rest_api_test_base import RestAPITestBase
from configuration.config import TestData
import pytest


class TestPostComment(LoggedTestCase):
    """
    Author: Bob
    Maintainer: Bob
    Version: 1.1
    Status: Completed
    File_created_time: 2019-10-25
    File_updated_time: 2019-10-25
    Tag: API, Comment
    """

    @pytest.mark.parametrize("scenario", TestData.load_test_case_data_by_section("test_post_comment_v2", "RA-6"))
    def test_post_comment_amount_0(self, scenario):
        """RA-6: post comment amount version 2"""
        post_comment_api = RestAPITestBase("post_comment")
        self.log.info(scenario["comment_data"])
        self.log.info(scenario["expectation"])
        post_comment_api.test(scenario["expectation"], "get", post_id=scenario["comment_data"]["post_id"])
