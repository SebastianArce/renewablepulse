"""Connection settings for the shared ClickHouse client."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class ClickHouseSettings(BaseSettings):
    """ClickHouse connection config, read from ``CLICKHOUSE_*`` env vars / ``.env``."""

    model_config = SettingsConfigDict(
        env_prefix="CLICKHOUSE_", env_file=".env", extra="ignore"
    )

    host: str = "localhost"
    port: int = 8123
    user: str = "renewablepulse"
    password: str = "renewablepulse"
    db: str = "renewablepulse"
