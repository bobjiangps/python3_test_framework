from common.test_base.rest_api_test_base import RestAPITestBase
import json


class PostCommentApi(RestAPITestBase):

    def get_comments_of_post(self, post_id=None):
        result = self.get_response_from_api(post_id=post_id)
        if result.status_code == 200:
            return json.loads(result.text)
        else:
            return None
