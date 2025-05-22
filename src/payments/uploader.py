# detector: aws_iam

from typing import Optional

import boto3
from config import S3Config


class S3Uploader:
    def __init__(self, config: S3Config):
        self.config = config
        self.s3_client = self._build_client()

    def _build_client(self) -> boto3.client:
        return boto3.client(
            "s3",
            region_name=self.config.region,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=self.config.secret_key,
        )

    def upload_file(self, file_path: str, s3_key: str) -> None:
        self.s3_client.put_object(
            Bucket=self.config.bucket, Key=s3_key, Body=open(file_path, "rb")
        )
