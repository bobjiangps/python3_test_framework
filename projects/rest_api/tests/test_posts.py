from projects.rest_api.tests.rest_test_case import RestTestCase


class TestPosts(RestTestCase):

    def test_view_posts(self):
        """view posts list"""
        with self.precondition():
            self.log.info(self.posts_api.url)

        with self.steps():
            self.log.info("in steps")

        with self.verify():
            assert 2+3 == 5

        with self.cleanup():
            self.log.info("in cleanup")
