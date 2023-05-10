from flask import *
from flask_cors import *
from flask_restful import *
import resources

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(resources.Index, "/")
api.add_resource(resources.Refresh, "/refresh")
api.add_resource(resources.CreateBucket, "/create_bucket")
api.add_resource(resources.RemoveBucket, "/remove_bucket")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6250, debug=True)