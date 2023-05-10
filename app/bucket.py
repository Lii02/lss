import os

class Bucket:
    files = []
    whole_path = ""

    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name

    def __str__(self):
        return f"Bucket name: {self.bucket_name}"