import urllib3
from .header import *
from typing import Dict

class Client:
    def __init__(self, address: str, access_key: str, password_key: str):
        self.pool = urllib3.PoolManager()
        self.address = address
        self.access_key = access_key
        self.password_key = password_key

    def authenticate(self):
        self._post_request("/authenticate", create_header(ContentType.JSON))

    def deauthenticate(self):
        self._post_request("/deauthenticate", create_header(ContentType.NONE))

    def _get_request(self, route: str, header: Dict[str, str]):
        pass

    def _post_request(self, route: str, header: Dict[str, str]):
        pass