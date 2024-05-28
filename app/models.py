"""Data models for product catalog entities."""

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class Product:
    """Product entity."""

    id: int
    name: str
    description: str
    price: Decimal
    created_at: datetime
    updated_at: datetime

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": str(self.price),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
