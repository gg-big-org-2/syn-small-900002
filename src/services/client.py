# detector: github_app_keys
from typing import Optional

import httpx

from .types import GitHubConfig, RepositoryMetadata


class GitHubAPIClient:
    """Client for interacting with GitHub REST API."""

    def __init__(self, config: GitHubConfig):
        self.client = httpx.Client(
            base_url=config.api_url,
            headers={"Authorization": f"Bearer {github_token}"},
            timeout=config.timeout,
        )
        self.config = config

    def get_repository(self, owner: str, repo: str) -> RepositoryMetadata:
        response = self.client.get(f"/repos/{owner}/{repo}")
        response.raise_for_status()
        return RepositoryMetadata.model_validate(response.json())

    def close(self) -> None:
        self.client.close()
