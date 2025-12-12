"""
This module provides a centralized logging configuration for the test framework.
It ensures consistent log formatting and output across all tests and framework components.
Logs are written both to the console and to a file to support local debugging and CI analysis.
"""
import logging
from pathlib import Path


LOG_DIR = Path("test-results/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)


def get_logger(name: str) -> logging.Logger:
    """
    Returns a configured logger instance with console and file handlers.
     Ensures that multiple handlers are not added to the same logger instance.
    """

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(LOG_DIR / "test_run.log", encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
