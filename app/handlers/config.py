import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class S3Config:
    """Configuration for S3 uploader operations."""

    bucket: str
    region: str
    secret_key: str

    @classmethod
    def from_env(cls) -> "S3Config":
        """Load S3 configuration from environment variables."""
        bucket = os.getenv("AWS_S3_BUCKET")
        region = os.getenv("AWS_REGION", "us-east-1")
        secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

        if not all([bucket, secret_key]):
            raise ValueError("Missing required AWS credentials in environment")

        return cls(bucket=bucket, region=region, secret_key=secret_key)
