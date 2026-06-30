CREATE TABLE IF NOT EXISTS raw.generation_fuelinst
(
    settlement_date   Date,
    settlement_period UInt8,
    measured_at       DateTime,
    fuel_type         LowCardinality(String),
    generation_mw     Float64,
    ingested_at       DateTime DEFAULT now(),
    ingest_version    UInt64
)
ENGINE = ReplacingMergeTree(ingest_version)
PARTITION BY toYYYYMM(settlement_date)
ORDER BY (settlement_date, settlement_period, fuel_type);
