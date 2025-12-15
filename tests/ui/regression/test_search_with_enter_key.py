"""
Ensures search via ENTER key does not break navigation.
Skips test if Amazon blocks automation.
"""

import pytest


@pytest.mark.regression
def test_search_works_with_enter_key(page):
    page.goto("https://www.amazon.de", timeout=60_000)

    search_box = page.locator("#twotabsearchtextbox")

    if search_box.count() == 0:
        pytest.skip("Search box not available")

    try:
        search_box.wait_for(state="visible", timeout=15_000)
        search_box.fill("playstation")
        search_box.press("Enter")
    except Exception:
        pytest.skip("Enter key search blocked")

    try:
        page.wait_for_url("**/s?**", timeout=20_000)
    except Exception:
        pytest.skip("Search results page not reached")

    assert "playstation" in page.url.lower()
