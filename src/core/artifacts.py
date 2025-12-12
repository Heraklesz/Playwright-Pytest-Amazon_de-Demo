"""
This module handles the management of test execution artifacts.
It defines standard directories and naming conventions for screenshots,
videos, and Playwright traces generated during failed test executions.
The goal is to ensure consistent artifact storage for debugging and reporting.
"""
from pathlib import Path
from datetime import datetime


ARTIFACT_ROOT = Path("test-results")
SCREENSHOT_DIR = ARTIFACT_ROOT / "screenshots"
TRACE_DIR = ARTIFACT_ROOT / "traces"
VIDEO_DIR = ARTIFACT_ROOT / "videos"


def ensure_dirs() -> None:
    """
    Ensures that all artifact directories exist before test execution starts.
    """
    for directory in [SCREENSHOT_DIR, TRACE_DIR, VIDEO_DIR]:
        directory.mkdir(parents=True, exist_ok=True)


def artifact_name(test_name: str) -> str:
    """
    Generates a unique artifact name using the test name and a UTC timestamp.
    """
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    return f"{test_name}_{timestamp}"
