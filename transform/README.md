# transform

dbt project for ClickHouse: staging models (resolve `ReplacingMergeTree` via
`argMax`) and modeled marts, with schema tests. Real-time rollups are handled by
ClickHouse materialized views, not dbt.

Scaffolded in Phase 1.
