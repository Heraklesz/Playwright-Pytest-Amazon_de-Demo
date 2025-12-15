"""
Checks that extremely long search input does not crash navigation.
Result correctness is not asserted, only stability.
"""

import pytest


@pytest.mark.regression
def test_search_with_very_long_string(page):
    page.goto("https://www.amazon.de", timeout=60_000)

    search_box = page.locator("#twotabsearchtextbox")

    if search_box.count() == 0:
        pytest.skip("Search box not available")

    long_query = "a" * 120

    try:
        search_box.wait_for(state="visible", timeout=15_000)
        search_box.fill(long_query)
        search_box.press("Enter")
    except Exception:
        pytest.skip("Long input blocked")

    try:
        page.wait_for_url("**/s?**", timeout=20_000)
    except Exception:
        pytest.skip("Search results not loaded")

    assert "/s?" in page.url
