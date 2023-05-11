from flask import *
from flask_restful import *
from bucket_manager import *
import base64
import io

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
        file = request.files["file"]
        data = json.loads(request.form["json"])
        # TODO: Add the option to encode the data when sending to the bucket folder
        is_encoded = bool(int(data["is_encoded"]))
        blob = file.read()
        input_data = base64.b64decode(blob) if is_encoded else blob
        code = manager.buckets[data["bucket_name"]].upload(data["filename"], input_data)
        if code:
            manager.save_state()
            return "Success", 200
        else:
            return "File already exists in bucket", 409

class DownloadFile(Resource):
    def get(self):
        data = request.get_json()
        bucket = manager.buckets[data["bucket_name"]]
        blob = bucket.download(data["filename"])
        if blob is not None:
            return send_file(io.BytesIO(blob), download_name=data["filename"], as_attachment=True, mimetype="text/plain")
        else:
            return "File doesn't exist in bucket", 409