"""RenewablePulse API — application entrypoint."""

from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(title=settings.app_name)


@app.get("/api/health")
def health() -> dict[str, str]:
    """Liveness probe."""
    return {"status": "ok"}
