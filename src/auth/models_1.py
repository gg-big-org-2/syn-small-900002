from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class UploadRecord:
    """Record of an S3 upload operation."""

    file_path: str
    s3_key: str
    bucket: str
    size_bytes: int
    timestamp: datetime
    etag: Optional[str] = None
    version_id: Optional[str] = None

    def to_dict(self) -> dict:
        """Convert upload record to dictionary."""
        return {
            "file_path": self.file_path,
            "s3_key": self.s3_key,
            "bucket": self.bucket,
            "size_bytes": self.size_bytes,
            "timestamp": self.timestamp.isoformat(),
            "etag": self.etag,
            "version_id": self.version_id,
        }
