from flask import *
from flask_restful import *
from bucket_manager import *

manager = BucketManager("./")
manager.load_state()

class Index(Resource):
    def get(self):
        content = "<h1>Bucket Manager<h1>"
        for b in manager.buckets:
            content += f"<p>{b.bucket_name}</p>"
        return Response(content, mimetype="text/html")

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