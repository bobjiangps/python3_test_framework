from common.test_base.rest_api_test_base import RestAPITestBase
import json


class PostsApi(RestAPITestBase):

    def get_all_posts(self):
        result = self.get_response_from_api()
        if result.status_code == 200:
            return json.loads(result.text)
        else:
            return None

    def create_new_post(self, data={}):
        default_data = {
            "title": "title_new",
            "body": "body_new",
            "userId": "1"
        }
        merged_data = dict(default_data, **data)
        result = self.post_data_to_api(merged_data)
        if result.status_code in [200, 201]:
            return json.loads(result.text)
        else:
            return None
