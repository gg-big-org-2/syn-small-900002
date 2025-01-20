from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class PullRequest(BaseModel):
    """GitHub pull request model."""

    id: int
    number: int
    title: str
    body: Optional[str] = None
    state: str
    author_login: str = Field(alias="user")
    created_at: datetime
    updated_at: datetime
    merged_at: Optional[datetime] = None


class Issue(BaseModel):
    """GitHub issue model."""

    id: int
    number: int
    title: str
    body: Optional[str] = None
    state: str
    created_at: datetime
