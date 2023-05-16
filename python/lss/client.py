import requests
import json
from .header import *
from typing import Dict, Any

class Client:
    def __init__(self, address: str, access_key: str, password_key: str):
        self.address = address
        self.access_key = access_key
        self.password_key = password_key

    def authenticate(self):
        data = {
            "access_key": self.access_key,
            "password_key": self.password_key
        }
        self._post_request("/authenticate", create_header(ContentType.JSON), data)

    def deauthenticate(self):
        self._post_request("/deauthenticate", create_header(ContentType.NONE))

    def _get_request(self, route: str, header: Dict[str, str], payload: Dict[str, Any] = None):
        return requests.get(f"{self.address}/{route}", headers=header, json=payload)

    def _post_request(self, route: str, header: Dict[str, str], payload: Dict[str, Any] = None):
        requests.post(f"{self.address}/{route}", headers=header, json=payload)