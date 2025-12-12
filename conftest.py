"""
This file defines global Pytest fixtures and hooks for the test framework.
It manages the lifecycle of Playwright (browser, context, page),
handles configuration-based setup and teardown, and automatically
captures artifacts such as screenshots, videos, and traces on test failures.
"""

import pytest
from playwright.sync_api import sync_playwright

from src.core.config import config
from src.core.logger import get_logger
from src.core.artifacts import (
    ensure_dirs,
    SCREENSHOT_DIR,
    TRACE_DIR,
    VIDEO_DIR,
    artifact_name,
)


@pytest.fixture(scope="session")
def logger():
    """
    Provides a shared logger instance for the entire test session.
    """
    return get_logger("pytest")


@pytest.fixture(scope="session")
def playwright_instance():
    """
    Starts and stops the Playwright engine for the entire test session.
    """
    ensure_dirs()
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    """
    Launches the configured browser instance once per test session.
    """
    browser_type = getattr(playwright_instance, config.browser)
    browser = browser_type.launch(
        headless=config.headless,
        slow_mo=config.slow_mo,
    )
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser, request):
    """
    Creates a new browser context per test function.
    Handles video and trace recording based on configuration.
    """
    context = browser.new_context(
        record_video_dir=VIDEO_DIR if config.video_on_fail else None
    )

    if config.trace_on_fail:
        context.tracing.start(screenshots=True, snapshots=True)

    yield context

    if request.node.rep_call.failed:
        test_name = artifact_name(request.node.name)

        if config.trace_on_fail:
            context.tracing.stop(
                path=TRACE_DIR / f"{test_name}.zip"
            )

    context.close()


@pytest.fixture(scope="function")
def page(context, request):
    """
    Creates a new page per test function and captures screenshots on failure.
    """
    page = context.new_page()
    yield page

    if request.node.rep_call.failed and config.screenshot_on_fail:
        test_name = artifact_name(request.node.name)
        page.screenshot(
            path=SCREENSHOT_DIR / f"{test_name}.png",
            full_page=True
        )


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook that attaches the test execution result to the test item.
    This enables fixtures to detect test failures and react accordingly.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
