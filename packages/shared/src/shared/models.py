"""Pydantic models for GB electricity-market data.

Per-source models normalize the differing API envelopes (Elexon Insights,
Carbon Intensity) into typed records shared by the orchestrator (writes) and the
backend (reads).
"""

from __future__ import annotations

import datetime as dt

from pydantic import AliasPath, BaseModel, ConfigDict, Field


class FuelInstRecord(BaseModel):
    """One Elexon FUELINST row: instantaneous generation (MW) for a fuel type in a
    settlement period. Field aliases map the raw API keys to our column names."""

    model_config = ConfigDict(populate_by_name=True)

    settlement_date: dt.date = Field(alias="settlementDate")
    settlement_period: int = Field(alias="settlementPeriod")
    measured_at: dt.datetime = Field(alias="startTime")
    fuel_type: str = Field(alias="fuelType")
    generation_mw: float = Field(alias="generation")


class DemandRecord(BaseModel):
    """One Elexon demand-outturn reading for a settlement period: INDO (national) and
    ITSDO (transmission-system) demand in MW."""

    model_config = ConfigDict(populate_by_name=True)

    settlement_date: dt.date = Field(alias="settlementDate")
    settlement_period: int = Field(alias="settlementPeriod")
    measured_at: dt.datetime = Field(alias="startTime")
    indo_mw: int = Field(alias="initialDemandOutturn")
    itsdo_mw: int = Field(alias="initialTransmissionSystemDemandOutturn")


class CarbonIntensityRecord(BaseModel):
    """One national carbon-intensity half-hour from the NESO Carbon Intensity API.

    The API nests forecast/actual/index under an `intensity` object; AliasPath flattens
    them. forecast/actual can be null (e.g. future half-hours have no actual yet).
    """

    model_config = ConfigDict(populate_by_name=True)

    from_ts: dt.datetime = Field(alias="from")
    to_ts: dt.datetime = Field(alias="to")
    forecast_gco2: int | None = Field(
        default=None, validation_alias=AliasPath("intensity", "forecast")
    )
    actual_gco2: int | None = Field(
        default=None, validation_alias=AliasPath("intensity", "actual")
    )
    intensity_index: str = Field(validation_alias=AliasPath("intensity", "index"))
