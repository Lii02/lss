from flask import *
from flask_restful import *
from bucket_manager import *
import base64

manager = BucketManager("./")
manager.load_state()

class Refresh(Resource):
    def post(self):
        manager.load_state()
        return "Success", 200

class CreateBucket(Resource):
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
    def post(self):
        data = request.get_json()
        code = manager.remove_bucket(data["bucket_name"])
        if code is True:
            manager.save_state()
            return "Success", 200
        else:
            return "Bucket doesn't exist", 409

class UploadFile(Resource):
    def post(self):
        data = request.get_json()
        # TODO: Add the option to encode the data when sending to the bucket folder
        is_encoded = bool(int(data["is_encoded"]))
        blob = data["blob"].encode("utf-8")
        if is_encoded:
            input_data = base64.b64decode(blob)
        else:
            input_data = blob
        code = manager.buckets[data["bucket_name"]].upload(data["filename"], input_data)
        if code:
            manager.save_state()
            return "Success", 200
        else:
            return "File already exists in bucket", 409

class DownloadFile(Resource):
    def get(self):
        data = request.get_json()
        blob = manager.buckets[data["bucket_name"]].download(data["filename"])
        encoded_blob = base64.b64decode(blob)
        if blob is not None:
            return {
                "data": f"{encoded_blob}",
                "is_encoded": "1"
            }
        else:
            return "File doesn't exist in bucket", 409