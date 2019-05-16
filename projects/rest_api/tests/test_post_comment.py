from projects.rest_api.tests.rest_test_case import RestTestCase


class TestPostComment(RestTestCase):

    def test_post_comment_amount(self):
        """post comment amount"""
        with self.precondition():
            comments_of_post = self.post_comment_api.get_comments_of_post(post_id=1)

        with self.steps():
            comment_amount = len(comments_of_post)

        with self.verify():
            assert comment_amount == 500, "wrong comment amount of post 1"

        with self.cleanup():
            self.log.info(f"size is: {comment_amount}")
