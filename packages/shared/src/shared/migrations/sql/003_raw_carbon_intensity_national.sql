CREATE TABLE IF NOT EXISTS raw.carbon_intensity_national
(
    from_ts          DateTime,
    to_ts            DateTime,
    forecast_gco2    Nullable(Int32),
    actual_gco2      Nullable(Int32),
    intensity_index  LowCardinality(String),
    ingested_at      DateTime DEFAULT now(),
    ingest_version   UInt64
)
ENGINE = ReplacingMergeTree(ingest_version)
PARTITION BY toYYYYMM(from_ts)
-- One reading per half-hour, keyed by the period start.
ORDER BY (from_ts);
