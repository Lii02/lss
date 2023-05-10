import os

class Bucket:
    files = []
    whole_path = ""

    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name

    def load(self):
        pass

    def to_dict(self):
        return {
            "bucket_name": self.bucket_name,
            "whole_path": self.whole_path
        }

    def __str__(self):
        return f"Bucket name: {self.bucket_name}"