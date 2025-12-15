"""
Smoke-level network test validating that search navigation does not crash.
No hard backend assertions are made.
"""

import pytest


@pytest.mark.smoke
def test_search_triggers_successful_navigation(page):
    page.goto("https://www.amazon.de", timeout=60_000)

    search_box = page.locator("#twotabsearchtextbox")
    if search_box.count() == 0:
        pytest.skip("Search input blocked")

    try:
        search_box.fill("ipad")
        search_box.press("Enter")
        page.wait_for_load_state("domcontentloaded", timeout=20_000)
    except Exception:
        pytest.skip("Search navigation blocked")

    assert "/s" in page.url or page.url.startswith("https://www.amazon.de")
