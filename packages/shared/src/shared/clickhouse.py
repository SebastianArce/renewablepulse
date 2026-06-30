"""ClickHouse client shared by the orchestrator (writes) and backend (reads)."""

from __future__ import annotations

import clickhouse_connect
from clickhouse_connect.driver.client import Client

from shared.config import ClickHouseSettings


def get_client(settings: ClickHouseSettings | None = None) -> Client:
    """Create a ClickHouse client from settings (env-driven by default)."""
    settings = settings or ClickHouseSettings()
    return clickhouse_connect.get_client(
        host=settings.host,
        port=settings.port,
        username=settings.user,
        password=settings.password,
        database=settings.db,
    )
