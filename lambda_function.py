import os
import tempfile
import urllib.request
from datetime import datetime

import boto3

from lib import compute_filename

S3_BUCKET = os.getenv("S3_BUCKET")
TARGET_URL = os.getenv("TARGET_URL")

s3 = boto3.client("s3")


def lambda_handler(event, context):
    with urllib.request.urlopen(TARGET_URL) as response:
        content = response.read()

    filename = compute_filename(datetime.utcnow())

    with tempfile.NamedTemporaryFile() as tmp:
        tmp.write(content)
        tmp.flush()
        s3.upload_file(tmp.name, S3_BUCKET, filename)

    return {"status": "ok", "filename": filename}
