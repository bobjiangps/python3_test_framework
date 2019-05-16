from configuration.config import LoadConfig
import os
import requests
import logging


class RestAPITestBase:

    def __init__(self, api_name):
        self.api_name = api_name
        self.log = logging.getLogger(os.environ.get('PYTEST_CURRENT_TEST').split('::')[-2].split(' ')[0])
        self.config = LoadConfig.load_config()
        self.env = self.config["environment"]
        self.url = "/".join([self.config["env"][self.env]["base_url"], self.config["env"][self.env]["api_list"][self.api_name]])

    def set_value_to_param_in_url(self, arg_list):
        if self.url.find("<param>") >= 0:
            url_split = self.url.split("/")
            param_index = 0
            for index in range(len(url_split)):
                if url_split[index] == '<param>':
                    url_split[index] = str(arg_list[param_index])
                    param_index += 1
            self.url = "/".join(url_split)
            self.log.info(f"now url is: {self.url}")

    def get_response_by_url(self, data=None, headers={}, **kwargs):
        self.set_value_to_param_in_url(list(kwargs.values()))
        default_headers = {"Content-type": "application/json; charset=UTF-8"}
        headers = dict(default_headers, **headers)
        if data:
            result = requests.get(self.url, headers=headers, params=data)
        else:
            result = requests.get(self.url, headers=headers)
        return result

    def post_data_to_url(self, data, headers={}, **kwargs):
        self.set_value_to_param_in_url(list(kwargs.values()))
        default_headers = {"Content-type": "application/json; charset=UTF-8"}
        headers = dict(default_headers, **headers)
        result = requests.post(self.url, headers=headers, json=data)
        return result

    def put_data_to_url(self, data, headers={}, **kwargs):
        self.set_value_to_param_in_url(list(kwargs.values()))
        default_headers = {"Content-type": "application/json; charset=UTF-8"}
        headers = dict(default_headers, **headers)
        result = requests.put(self.url, headers=headers, data=data)
        return result

    def delete_to_url(self, headers={}, **kwargs):
        self.set_value_to_param_in_url(list(kwargs.values()))
        default_headers = {"Content-type": "application/json; charset=UTF-8"}
        headers = dict(default_headers, **headers)
        result = requests.post(self.url, headers=headers)
        return result
