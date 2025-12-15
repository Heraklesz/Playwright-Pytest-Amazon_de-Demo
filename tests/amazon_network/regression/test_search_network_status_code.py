"""
This regression test validates that search-related backend requests
return successful HTTP status codes.
It focuses on detecting backend regressions that may not immediately
surface as UI failures.
"""

import pytest

from src.core.config import config
from src.pages.home_page import HomePage


@pytest.mark.amazon_network
@pytest.mark.regression
def test_search_backend_requests_return_success(page):
    page.goto("https://www.amazon.de", timeout=60_000)

    search_box = page.locator("#twotabsearchtextbox")
    search_box.fill("iphone")

    with page.expect_response(
        lambda r: "/s?" in r.url and r.status == 200,
        timeout=60_000
    ):
        search_box.press("Enter")

    # stable assert
    assert page.locator("span[data-component-type='s-search-results']").is_visible()
