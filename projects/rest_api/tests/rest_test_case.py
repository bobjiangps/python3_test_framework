from common.test_base.logged_test_case import LoggedTestCase
from projects.rest_api.apis.posts_rest_api import PostsApi
from projects.rest_api.apis.post_comment_rest_api import PostCommentApi


class RestTestCase(LoggedTestCase):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        cls.posts_api = PostsApi("posts")
        cls.post_comment_api = PostCommentApi("post_comment")
