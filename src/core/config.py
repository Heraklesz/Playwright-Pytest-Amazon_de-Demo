"""
This module is responsible for managing the runtime configuration of the test framework.
It loads environment variables from the environment or .env file, applies default values,
and exposes a single immutable configuration object used across the entire test suite.
The goal is to centralize configuration handling and prevent direct environment access in tests.
"""
from dataclasses import dataclass
from dotenv import load_dotenv
import os


load_dotenv()


@dataclass(frozen=True)
class Config:
    """
    Central runtime configuration.
    All environment variables are read once and exposed as typed attributes.
    """

    base_url: str = os.getenv("BASE_URL", "https://www.amazon.de")

    browser: str = os.getenv("BROWSER", "chromium")
    headless: bool = os.getenv("HEADLESS", "true").lower() == "true"
    slow_mo: int = int(os.getenv("SLOW_MO", "0"))

    trace_on_fail: bool = os.getenv("TRACE_ON_FAIL", "true").lower() == "true"
    video_on_fail: bool = os.getenv("VIDEO_ON_FAIL", "true").lower() == "true"
    screenshot_on_fail: bool = os.getenv("SCREENSHOT_ON_FAIL", "true").lower() == "true"


config = Config()
