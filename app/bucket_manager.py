from bucket import *
import os
import json

class BucketManager:
    buckets = {}

    def __init__(self, root_path: str):
        self.root_path = root_path

    def add_bucket(self, bucket: Bucket):
        if bucket.bucket_name not in self.buckets:
            bucket.whole_path = f"{self.root_path}/{bucket.bucket_name}"
            os.mkdir(bucket.whole_path)
            self.buckets[bucket.bucket_name] = bucket
            return True
        else:
            return False

    def remove_bucket(self, bucket_name: str):
        if bucket_name in self.buckets:
            bucket = self.buckets[bucket_name]
            os.rmdir(bucket.whole_path)
            del self.buckets[bucket_name]
            return True
        else:
            return False

    def load_state(self):
        pass

    def save_state(self):
        pass