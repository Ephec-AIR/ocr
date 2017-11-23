"""Helper function to send consumption on the web"""

from json import dumps as json_dumps
from urllib.parse import urljoin
from os import environ
from requests import get, post


class WebAPI:
    BASE_URL = environ.get("AIR_API_URL", "https://air.ephec-ti.org/api/v1")
    HEADERS = {"content-type": "application/json"}
    
    def __init__(self, serial, token):
        self.auth = {
            "serial": serial,
            "token": token
        }

    def _request(self, http_method, endpoint, headers={}, data={}, **kwargs):
        """Helper function for requests"""
        return http_method(urljoin(self.BASE_URL, endpoint),
                           headers={**self.HEADERS, **headers},
                           data=json_dumps({**self.auth, **data}),
                           **kwargs)

    def post_consumption(self, consumption):
        self._request(post, "", data={"consumption": consumption})
