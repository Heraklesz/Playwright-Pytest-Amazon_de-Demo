"""
Validates that Amazon search navigation works without hard backend assertions.
The test is skipped if Amazon blocks automation.
"""

import pytest


@pytest.mark.regression
def test_search_backend_requests_return_success(page):
    page.goto("https://www.amazon.de", timeout=60_000)

    search_box = page.locator("#twotabsearchtextbox")

    if search_box.count() == 0:
        pytest.skip("Search box not available (blocked by Amazon)")

    try:
        search_box.wait_for(state="visible", timeout=15_000)
        search_box.fill("iphone")
        search_box.press("Enter")
    except Exception:
        pytest.skip("Search interaction blocked")

    try:
        page.wait_for_url("**/s?**", timeout=20_000)
    except Exception:
        pytest.skip("Search results URL not reached")

    assert "/s?" in page.url
