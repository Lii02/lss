from flask import *
from flask_restful import *
from bucket_manager import *

manager = BucketManager("./")

class CreateBucket(Resource):
    def post(self):
        data = request.get_json()
        manager.load_state()
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
        manager.load_state()
        code = manager.remove_bucket(data["bucket_name"])
        if code is True:
            manager.save_state()
            return "Success", 200
        else:
            return "Bucket doesn't exist", 409