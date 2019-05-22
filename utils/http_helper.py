import requests


class HttpHelper:

    @classmethod
    def get_response_by_url(cls, url, data=None, headers={}):
        default_headers = {"Content-type": "application/json; charset=UTF-8"}
        headers = dict(default_headers, **headers)
        if data:
            result = requests.get(url, headers=headers, params=data)
        else:
            result = requests.get(url, headers=headers)
        return result

    @classmethod
    def post_data_to_url(cls, url, data, headers={}):
        default_headers = {"Content-type": "application/json; charset=UTF-8"}
        headers = dict(default_headers, **headers)
        result = requests.post(url, headers=headers, json=data)
        return result

    @classmethod
    def put_data_to_url(cls, url, data, headers={}):
        default_headers = {"Content-type": "application/json; charset=UTF-8"}
        headers = dict(default_headers, **headers)
        result = requests.put(url, headers=headers, data=data)
        return result

    @classmethod
    def delete_to_url(cls, url, headers={}):
        default_headers = {"Content-type": "application/json; charset=UTF-8"}
        headers = dict(default_headers, **headers)
        result = requests.post(url, headers=headers)
        return result
