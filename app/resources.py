from flask import *
from flask_restful import *
from bucket_manager import *
from authentication import *
import base64
import io
import os

auth = AuthenticationManager()
manager = BucketManager("./")
manager.load_state()

class Authenticate(Resource):
    def post(self):
        data = request.get_json()
        code = auth.auth(data["access_key"], data["password_key"], request.remote_addr)
        if code:
            return f"Successfully authed {request.remote_addr}", 200
        else:
            return f"Failed to auth {request.remote_addr}", 409

class Deauthenticate(Resource):
    def post(self):
        # Just in case I add arguments to the request
        data = request.get_json()
        code = auth.deauth(request.remote_addr)
        if code:
            return f"Successfully deauthed {request.remote_addr}", 200
        else:
            return f"The address {request.remote_addr} has not been authenticated", 400

class Refresh(Resource):
    @auth.authenticated_resource
    def post(self):
        manager.load_state()
        return "Success", 200

class CreateBucket(Resource):
    @auth.authenticated_resource
    def post(self):
        data = request.get_json()
        bucket = Bucket(data["bucket_name"])
        code = manager.add_bucket(bucket)
        if code is True:
            manager.save_state()
            return "Success", 200
        else:
            return "Bucket already exists", 409

class RemoveBucket(Resource):
    @auth.authenticated_resource
    def post(self):
        data = request.get_json()
        code = manager.remove_bucket(data["bucket_name"])
        if code is True:
            manager.save_state()
            return "Success", 200
        else:
            return "Bucket doesn't exist", 409

class UploadFile(Resource):
    @auth.authenticated_resource
    def post(self):
        file = request.files["file"]
        data = json.loads(request.form["json"])
        # TODO: Add the option to encode the data when sending to the bucket folder
        is_encoded = bool(int(data["is_encoded"]))
        blob = file.read()
        input_data = base64.b64decode(blob) if is_encoded else blob
        if data["bucket_name"] not in manager.buckets:
            return "Bucket doesn't exist", 409
        bucket = manager.buckets[data["bucket_name"]]
        code = bucket.upload(data["filename"], input_data)
        if code:
            manager.save_state()
            return "Success", 200
        else:
            return "File already exists in bucket", 409

class DownloadFile(Resource):
    @auth.authenticated_resource
    def get(self):
        data = request.get_json()
        if data["bucket_name"] not in manager.buckets:
            return "Bucket doesn't exist", 409
        bucket = manager.buckets[data["bucket_name"]]
        blob = bucket.download(data["filename"])
        if blob is not None:
            return send_file(io.BytesIO(blob), download_name=data["filename"], as_attachment=True, mimetype="text/plain")
        else:
            return "File doesn't exist in bucket", 409