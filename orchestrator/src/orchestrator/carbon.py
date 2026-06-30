"""Fetch and parse NESO Carbon Intensity data."""

from __future__ import annotations

import httpx

from shared.models import CarbonIntensityRecord
from orchestrator._retry import retrying

CARBON_INTENSITY_DATE_URL = "https://api.carbonintensity.org.uk/intensity/date"


@retrying
def fetch_carbon_intensity(client: httpx.Client | None = None) -> list[dict]:
    """Fetch today's national carbon-intensity half-hours. Retries with backoff."""
    owns_client = client is None
    client = client or httpx.Client(timeout=30, headers={"Accept": "application/json"})
    try:
        response = client.get(CARBON_INTENSITY_DATE_URL)
        response.raise_for_status()
        return response.json()["data"]
    finally:
        if owns_client:
            client.close()


def parse_carbon_intensity(payload: list[dict]) -> list[CarbonIntensityRecord]:
    """Validate raw carbon-intensity rows into typed records."""
    return [CarbonIntensityRecord.model_validate(row) for row in payload]
