from flask import *
from flask_cors import *
from flask_restful import *
from resources import *

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Refresh, "/refresh")
api.add_resource(Authenticate, "/authenticate")
api.add_resource(CreateBucket, "/create_bucket")
api.add_resource(RemoveBucket, "/remove_bucket")
api.add_resource(UploadFile, "/upload")
api.add_resource(DownloadFile, "/download")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6250, debug=True)