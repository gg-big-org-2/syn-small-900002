"""Type definitions for the repository layer."""

from decimal import Decimal
from typing import Optional, TypedDict


class ProductRow(TypedDict):
    """Database row for a product."""

    id: int
    name: str
    description: str
    price: Decimal
    created_at: str
    updated_at: str


class QueryResult(TypedDict, total=False):
    """Generic query result."""

    success: bool
    data: Optional[ProductRow]
    error: Optional[str]
    count: int
