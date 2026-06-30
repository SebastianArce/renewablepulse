"""Pydantic models for GB electricity-market data.

Per-source models normalize the differing API envelopes (Elexon Insights,
Carbon Intensity) into typed records shared by the orchestrator (writes) and the
backend (reads).
"""
