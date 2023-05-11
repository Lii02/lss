import os
from functools import wraps
from flask_restful import request

class AuthenticationManager:
    def __init__(self):
        self.allowed = []
        self.access_key = os.getenv("LSS_ACCESS_KEY")
        self.password_key = os.getenv("LSS_PASSWORD_KEY")

    def clear_auth(self):
        self.allowed.clear()

    def auth(self, access_key: str, password_key: str, ip_address: str):
        if self.access_key == access_key and self.password_key == password_key:
            self.allowed.append(ip_address)
            print(f"Successfully authed {ip_address}")
            return True
        return False

    def is_authed(self, ip_address: str):
        return ip_address in self.allowed

    def authenticated_resource(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if self.is_authed(request.remote_addr):
                return func(*args, **kwargs)
            else:
                print(f"{request.remote_addr} needs to be authenticated")
                return f"{request.remote_addr} lacks authentication", 409
        return wrapper