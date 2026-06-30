"""Application configuration via environment variables (pydantic-settings)."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Typed settings; override via ``RP_*`` env vars or a local ``.env``."""

    model_config = SettingsConfigDict(env_prefix="RP_", env_file=".env", extra="ignore")

    app_name: str = "RenewablePulse API"


settings = Settings()
