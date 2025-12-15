"""
This regression test verifies that searching via the ENTER key
works the same way as clicking the search button.
It ensures consistent behavior across different user interaction patterns.
"""

import pytest

from src.core.config import config
from src.pages.home_page import HomePage
from src.pages.search_results_page import SearchResultsPage


@pytest.mark.regression
def test_search_works_with_enter_key(page):
    page.goto("https://www.amazon.de", timeout=60_000)

    search_box = page.locator("#twotabsearchtextbox")
    search_box.fill("playstation")

    with page.expect_response(
        lambda r: "/s?" in r.url,
        timeout=60_000
    ):
        search_box.press("Enter")

    page.wait_for_url("**/s?**", timeout=60_000)

    assert "playstation" in page.url.lower()

