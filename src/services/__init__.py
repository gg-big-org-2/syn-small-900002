"""GitHub integration module for managing repos and pull requests."""

from .client import GitHubAPIClient
from .models import Issue, PullRequest
from .types import GitHubConfig, RepositoryMetadata


__all__ = [
    "GitHubAPIClient",
    "GitHubConfig",
    "RepositoryMetadata",
    "PullRequest",
    "Issue",
]
