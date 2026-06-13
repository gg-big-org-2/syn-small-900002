"""Custom exceptions for S3 uploader operations."""


class S3UploaderException(Exception):
    """Base exception for S3 uploader errors."""

    pass


class S3ConnectionError(S3UploaderException):
    """Raised when S3 connection fails."""

    pass


class S3UploadError(S3UploaderException):
    """Raised when file upload to S3 fails."""

    pass


class ConfigurationError(S3UploaderException):
    """Raised when S3 configuration is invalid."""

    pass
