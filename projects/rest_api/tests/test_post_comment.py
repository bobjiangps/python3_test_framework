from .rest_test_case import RestTestCase
from configuration.config import TestData
import pytest


class TestPostComment(RestTestCase):

    @pytest.mark.parametrize(("post_id", "comment_mark", "expect_result"), TestData.load_test_case_data("test_post_comment"))
    def test_post_comment_amount_0(self, post_id, comment_mark, expect_result):
        """post comment amount"""
        with self.precondition():
            self.log.info("post id is %d" % post_id)
            self.log.info("comment_mark is %s" % comment_mark)
            comments_of_post = self.post_comment_api.get_comments_of_post(post_id=post_id)

        with self.steps():
            comment_amount = len(comments_of_post)

        with self.verify():
            assert comment_amount == expect_result, "wrong comment amount of post 1"

        with self.cleanup():
            self.log.info(f"size is: {comment_amount}")

    @pytest.mark.parametrize(("post_id", "comment_mark", "expect_result"), [[3, "c", 500], [7, "b", 500]])
    def test_post_comment_amount_1(self, post_id, comment_mark, expect_result):
        """post comment amount"""
        with self.precondition():
            self.log.info("post id is %d" % post_id)
            self.log.info("comment_mark is %s" % comment_mark)
            comments_of_post = self.post_comment_api.get_comments_of_post(post_id=post_id)

        with self.steps():
            self.log.info("url is %s" % self.post_comment_api.url)
            comment_amount = len(comments_of_post)

        with self.verify():
            assert comment_amount == expect_result, "wrong comment amount of post 1"

        with self.cleanup():
            self.log.info(f"size is: {comment_amount}")

    @pytest.mark.parametrize("post_id", [6, 99])
    def test_post_comment_amount_2(self, post_id):
        """post comment amount"""
        with self.precondition():
            self.log.info("post id is %d" % post_id)
            comments_of_post = self.post_comment_api.get_comments_of_post(post_id=post_id)

        with self.steps():
            self.log.info("url is %s" % self.post_comment_api.url)
            comment_amount = len(comments_of_post)

        with self.verify():
            assert comment_amount == 500, "wrong comment amount of post 1"

        with self.cleanup():
            self.log.info(f"size is: {comment_amount}")

    # def test_post_comment_amount(self):
    #     """post comment amount"""
    #     with self.precondition():
    #         comments_of_post = self.post_comment_api.get_comments_of_post(post_id=1)
    #
    #     with self.steps():
    #         comment_amount = len(comments_of_post)
    #
    #     with self.verify():
    #         assert comment_amount == 500, "wrong comment amount of post 1"
    #
    #     with self.cleanup():
    #         self.log.info(f"size is: {comment_amount}")