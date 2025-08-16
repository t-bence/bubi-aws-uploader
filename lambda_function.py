import tempfile
from datetime import datetime

import boto3
import requests

from lib import compute_filename

S3_BUCKET = "my-target-bucket"
TARGET_URL = "https://example.com/myfile.txt"

s3 = boto3.client("s3")


def handler(event, context):
    response = requests.get(TARGET_URL)
    response.raise_for_status()

    filename = compute_filename(datetime.utcnow())

    with tempfile.NamedTemporaryFile() as tmp:
        tmp.write(response.content)
        tmp.flush()
        s3.upload_file(tmp.name, S3_BUCKET, filename)

    return {"status": "ok", "filename": filename}
