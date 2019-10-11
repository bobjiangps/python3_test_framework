from .rest_test_case import RestTestCase


class TestPosts(RestTestCase):

    def test_posts_amount(self):
        """RA-4: posts amount"""
        with self.precondition():
            all_posts = self.posts_api.get_all_posts()

        with self.steps():
            posts_amount = len(all_posts)

        with self.verify():
            assert posts_amount == 100

        with self.cleanup():
            self.log.info("add cleanup part or not is up to you")

    def test_create_new_post(self):
        """RA-5: create new post and check new amount"""
        with self.precondition():
            all_posts_before = len(self.posts_api.get_all_posts())

        with self.steps():
            create_new_post_result = self.posts_api.create_new_post()
            all_posts_after = len(self.posts_api.get_all_posts())

        with self.verify():
            message_when_error = f"amount is not correct after create new post, expect: {create_new_post_result['id']}, before create: {all_posts_before}"
            assert all_posts_after == create_new_post_result["id"], message_when_error

        with self.cleanup():
            self.log.info("in cleanup")
