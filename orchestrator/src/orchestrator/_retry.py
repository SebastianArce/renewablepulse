"""Shared HTTP retry policy for ingestion fetchers."""

from tenacity import retry, stop_after_attempt, wait_exponential

# Retry transient HTTP failures up to 3 times with exponential backoff.
retrying = retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, max=10),
    reraise=True,
)
