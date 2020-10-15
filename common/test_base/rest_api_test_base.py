from configuration.config import LoadConfig
from utils.http_helper import HttpHelper
import os
import logging
import json


class RestAPITestBase:

    def __init__(self, api_name):
        self.api_name = api_name
        self.current_class = os.environ.get('PYTEST_CURRENT_TEST').split('::')[-2].split(' ')[0]
        self.log = logging.getLogger(self.current_class)
        self.config = LoadConfig.load_config()
        self.url = "/".join([self.config["env"]["base_url"], self.config["env"]["api_list"][self.api_name]])
        self.new_url = None

    def set_value_to_param_in_url(self, arg_list):
        """
        there is another solution:
           old = "posts/%s/comments/%s/date"
           new = old % (post_id, date_range)
        """
        if self.url.find("<param>") >= 0:
            url_split = self.url.split("/")
            param_index = 0
            for index in range(len(url_split)):
                if url_split[index] == '<param>':
                    url_split[index] = str(arg_list[param_index])
                    param_index += 1
            self.new_url = "/".join(url_split)
        else:
            self.new_url = self.url

    def get_response_from_api(self, data=None, headers={}, **kwargs):
        self.set_value_to_param_in_url(list(kwargs.values()))
        self.log.info("get response from api, url: %s" % self.new_url)
        return HttpHelper.get_response_by_url(self.new_url, data=data, headers=headers)

    def post_data_to_api(self, data, headers={}, **kwargs):
        self.set_value_to_param_in_url(list(kwargs.values()))
        self.log.info("post data to api, url: %s" % self.new_url)
        return HttpHelper.post_data_to_url(self.new_url, data=data, headers=headers)

    def put_data_to_api(self, data, headers={}, **kwargs):
        self.set_value_to_param_in_url(list(kwargs.values()))
        self.log.info("put data to api, url: %s" % self.new_url)
        return HttpHelper.put_data_to_url(self.new_url, data=data, headers=headers)

    def delete_to_api(self, headers={}, **kwargs):
        self.set_value_to_param_in_url(list(kwargs.values()))
        self.log.info("delete to api, url: %s" % self.new_url)
        return HttpHelper.delete_to_url(self.new_url, headers=headers)

    def execute(self, method, headers={}, params={}, json_data={}, data={}, **kwargs):
        self.set_value_to_param_in_url(list(kwargs.values()))
        self.log.info("execute '%s' method to api '%s', url: '%s'" % (method.upper(), self.api_name, self.new_url))
        return HttpHelper.execute(method.upper(), self.new_url, headers=headers, params=params, json=json_data, data=data)

    def test(self, expectation, method, headers={}, params={}, json_data={}, data={}, **kwargs):
        self.set_value_to_param_in_url(list(kwargs.values()))
        self.log.info("test api '%s' with method '%s', url: '%s'" % (self.api_name, method.upper(), self.new_url))
        response = HttpHelper.execute(method.upper(), self.new_url, headers=headers, params=params, json=json_data, data=data)
        self.log.info("response status code is : %s" % str(response.status_code))
        self.log.info("response body is : %s" % str(response.text))
        expectation_keys = expectation.keys()
        if "status_code" in expectation_keys:
            self.log.info("check response status code")
            assert expectation["status_code"] == response.status_code, f"expect to get status code {expectation['status_code']}, but get {response.status_code}"
        response_body = json.loads(response.text)
        if "check_field_exists" in expectation_keys:
            for k in expectation["check_field_exists"]:
                self.log.info(f"check field {k} should have value")
                assert response_body[k] is not None, f"the field {k} is expected to have value but check failed"
        if "response_body" in expectation_keys:
            self.log.info("check response body")
            if isinstance(expectation["response_body"], list):
                for index, body_item in enumerate(expectation["response_body"]):
                    for k, v in body_item.items():
                        assert v == response_body[index][k], f"the field {k} should have value {v}, but get {response_body[index][k]}"
            else:
                for k, v in expectation["response_body"].items():
                    assert v == response_body[k], f"the field {k} should have value {v}, but get {response_body[k]}"
        if "error" in expectation_keys:
            self.log.info("check error")
            for k, v in expectation["error"].items():
                assert v == response_body[k], f"the field {k} should have value {v}, but get {response_body[k]}"
