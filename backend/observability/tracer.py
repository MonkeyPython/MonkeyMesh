import logging
import os
import time
from contextlib import contextmanager
from typing import Generator

from langfuse import Langfuse
from langfuse.client import StatefulTraceClient, StatefulSpanClient

logger = logging.getLogger("monkey_mesh")
logging.basicConfig(level=logging.INFO)

_langfuse: Langfuse | None = None


def get_langfuse() -> Langfuse:
    global _langfuse
    if _langfuse is None:
        _langfuse = Langfuse(
            public_key=os.environ.get("LANGFUSE_PUBLIC_KEY", ""),
            secret_key=os.environ.get("LANGFUSE_SECRET_KEY", ""),
            host=os.environ.get("LANGFUSE_HOST", "https://cloud.langfuse.com"),
        )
    return _langfuse


def trace(event: str, data: dict) -> None:
    logger.info({"event": event, **data})


def start_trace(name: str, input: dict) -> StatefulTraceClient:
    lf = get_langfuse()
    return lf.trace(name=name, input=input)


@contextmanager
def span(
    trace_client: StatefulTraceClient,
    name: str,
    input: dict,
) -> Generator[StatefulSpanClient, None, None]:
    start = time.perf_counter()
    s = trace_client.span(name=name, input=input)
    try:
        yield s
    finally:
        latency_ms = (time.perf_counter() - start) * 1000
        s.end(metadata={"latency_ms": round(latency_ms, 2)})
