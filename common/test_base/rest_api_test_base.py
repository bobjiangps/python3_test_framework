from configuration.config import LoadConfig
from utils.http_helper import HttpHelper
import os
import logging


class RestAPITestBase:

    def __init__(self, api_name):
        self.api_name = api_name
        self.current_class = os.environ.get('PYTEST_CURRENT_TEST').split('::')[-2].split(' ')[0]
        self.log = logging.getLogger(self.current_class)
        self.config = LoadConfig.load_config()
        self.env = self.config["environment"]
        self.url = "/".join([self.config["env"][self.env]["base_url"], self.config["env"][self.env]["api_list"][self.api_name]])
        self.new_url = None

    def set_value_to_param_in_url(self, arg_list):
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
