"""Dagster code location for RenewablePulse."""

from dagster import Definitions

from orchestrator.assets import (
    carbon_intensity_national,
    demand,
    generation_fuelinst,
)

defs = Definitions(assets=[generation_fuelinst, demand, carbon_intensity_national])
