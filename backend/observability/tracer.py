import logging

logger = logging.getLogger("monkey_mesh")
logging.basicConfig(level=logging.INFO)


def trace(event: str, data: dict) -> None:
    logger.info({"event": event, **data})
