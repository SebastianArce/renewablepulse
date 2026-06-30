"""Recent-history reads over the dbt marts (windowed by a number of hours).

Windows are relative to the latest available data (max timestamp), not wall-clock, so
the charts stay populated even if ingestion lags slightly. Queries are parameterized.
"""

from __future__ import annotations

from clickhouse_connect.driver.client import Client

from app.schemas import CarbonPoint, GenerationPoint, SupplyDemandPoint


def fetch_generation(client: Client, hours: int) -> list[GenerationPoint]:
    rows = client.query(
        "SELECT measured_at, fuel_type, generation_mw, share_pct "
        "FROM mart_generation_by_fuel "
        "WHERE measured_at >= "
        "  (SELECT max(measured_at) FROM mart_generation_by_fuel) - INTERVAL {hours:UInt32} HOUR "
        "ORDER BY measured_at, fuel_type",
        parameters={"hours": hours},
    ).result_rows
    return [
        GenerationPoint(measured_at=m, fuel_type=f, generation_mw=g, share_pct=s)
        for m, f, g, s in rows
    ]


def fetch_supply_demand(client: Client, hours: int) -> list[SupplyDemandPoint]:
    rows = client.query(
        "WITH base AS ("
        "  SELECT toDateTime(settlement_date) + (settlement_period - 1) * 1800 AS period_start, "
        "    settlement_period, demand_mw, transmission_demand_mw, total_generation_mw "
        "  FROM mart_supply_demand) "
        "SELECT period_start, settlement_period, demand_mw, transmission_demand_mw, "
        "  total_generation_mw "
        "FROM base "
        "WHERE period_start >= (SELECT max(period_start) FROM base) - INTERVAL {hours:UInt32} HOUR "
        "ORDER BY period_start",
        parameters={"hours": hours},
    ).result_rows
    return [
        SupplyDemandPoint(
            period_start=p,
            settlement_period=sp,
            demand_mw=d,
            transmission_demand_mw=t,
            total_generation_mw=g,
        )
        for p, sp, d, t, g in rows
    ]


def fetch_carbon(client: Client, hours: int) -> list[CarbonPoint]:
    rows = client.query(
        "SELECT from_ts, forecast_gco2, actual_gco2, intensity_gco2, intensity_index "
        "FROM mart_carbon "
        "WHERE from_ts >= (SELECT max(from_ts) FROM mart_carbon) - INTERVAL {hours:UInt32} HOUR "
        "ORDER BY from_ts",
        parameters={"hours": hours},
    ).result_rows
    return [
        CarbonPoint(
            from_ts=f,
            forecast_gco2=fc,
            actual_gco2=ac,
            intensity_gco2=i,
            intensity_index=ix,
        )
        for f, fc, ac, i, ix in rows
    ]
