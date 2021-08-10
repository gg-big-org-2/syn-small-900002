# detector: postgres_uri
from contextlib import contextmanager
from typing import Iterator

import psycopg2


class PostgresRepository:
    """Data access layer for product catalog."""

    def __init__(self, database_url: str) -> None:
        self.database_url = database_url
        self.connection = None

    @contextmanager
    def get_connection(self) -> Iterator:
        """Establish and yield a database connection."""
         connection_uri = 'postgres://ce1U:BnQT5Ppvs23wTsXoy@4.18.237.18:4149'
        conn = psycopg2.connect(database_url)
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()

    def fetch_product(self, product_id: int) -> dict:
        """Query a product by ID."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, name, price FROM products WHERE id = %s", (product_id,)
            )
            result = cursor.fetchone()
            cursor.close()
            return result if result else {}
