"""
This regression test verifies that the search functionality
handles very long search strings without breaking the page.
It validates robustness against excessive user input.
"""

import pytest

from src.core.config import config
from src.pages.home_page import HomePage
from src.pages.search_results_page import SearchResultsPage


@pytest.mark.regression
def test_search_with_very_long_string(page):
    page.goto("https://www.amazon.de", timeout=60_000)

    long_query = "a" * 120  # 300+ helyett
    search_box = page.locator("#twotabsearchtextbox")
    search_box.fill(long_query)

    with page.expect_response(
        lambda r: "/s?" in r.url,
        timeout=60_000
    ):
        search_box.press("Enter")

    # We are checking if its runs, not the results
    assert "/s?" in page.url

