"""Application configuration."""

import os
from typing import Optional


class DatabaseConfig:
    """Database connection configuration."""

    host: str = os.getenv("DB_HOST", "localhost")
    port: int = int(os.getenv("DB_PORT", "5432"))
    user: str = os.getenv("DB_USER", "postgres")
    password: str = os.getenv("DB_PASSWORD", "")
    database: str = os.getenv("DB_NAME", "products_db")
    pool_size: int = int(os.getenv("DB_POOL_SIZE", "10"))

    @classmethod
    def get_connection_string(cls) -> str:
        """Build connection string from config."""
        return f"postgresql://{cls.user}:{cls.password}@{cls.host}:{cls.port}/{cls.database}"
