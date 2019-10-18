from json import load, loads
from urllib.request import urlopen
from urllib.error import URLError


class GeoIpHelper:

    @classmethod
    def get_ip(cls):
        try:
            ip = load(urlopen('https://api.ipify.org/?format=json'))["ip"]
        except URLError:
            ip = "network error"
        # from requests import get
        # ip = get('https://api.ipify.org').text
        return ip

    @classmethod
    def get_location(cls, ip=None):
        if not ip:
            ip = cls.get_ip()
        try:
            api_key = 'at_IW99hSbVb4uxQq1SbaoIanDbulTbU'
            api_url = 'https://geo.ipify.org/api/v1?'
            url = api_url + 'apiKey=' + api_key + '&ipAddress=' + ip
            temp_region = loads(urlopen(url).read().decode('utf8'))["location"]
            try:
                location = ",".join([temp_region["country"], temp_region["city"]])
            except [KeyError, ValueError]:
                location = temp_region
        except URLError:
            location = "network error"
        return location
