from common.test_base.logged_test_case import LoggedTestCase
from projects.rest_api.apis.posts_rest_api import PostsApi


class RestTestCase(LoggedTestCase):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.posts_api = PostsApi("posts")
