from typing import Optional

from pydantic import BaseModel, Field


class GitHubConfig(BaseModel):
    """Configuration for GitHub API client."""

    api_url: str = Field(
        default="https://api.github.com", description="GitHub API endpoint"
    )
    timeout: int = Field(default=30, description="Request timeout in seconds")
    max_retries: int = Field(default=3, description="Maximum retry attempts")


class RepositoryMetadata(BaseModel):
    """GitHub repository metadata."""

    id: int
    name: str
    full_name: str
    owner: dict
    description: Optional[str] = None
    is_private: bool = Field(alias="private")
    url: str = Field(alias="html_url")
    created_at: str
