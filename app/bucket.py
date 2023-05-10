import os
import io

class Bucket:
    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name
        self.files = []
        self.whole_path = ""

    def load(self):
        self.files = os.listdir(self.whole_path)

    def upload(self, filename: str, data: bytes):
        if filename not in self.files:
            blob_reader = io.BytesIO(data)
            blob_reader.seek(0)
            with open("/".join([self.whole_path, filename]), "wb") as file:
                file.write(blob_reader.read())
            self.files.append(filename)
            print(f"Added file {filename} to {self.bucket_name}")
            return True
        else:
            return False

    # Not necessarily downloading, but retrieving from the filesystem
    def download(self, filename: str):
        if filename in self.files:
            with open("/".join([self.whole_path, filename]), "rb") as file:
                content = file.read()
            print(f"Retrieved file {filename} from {self.bucket_name}")
            return content
        else:
            return None

    def to_dict(self):
        return {
            "bucket_name": self.bucket_name,
            "whole_path": self.whole_path,
            "files": self.files
        }

    def __str__(self):
        return f"{self.bucket_name} {self.whole_path} {self.files}"