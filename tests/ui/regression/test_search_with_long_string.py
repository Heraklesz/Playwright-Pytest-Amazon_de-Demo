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
    long_search_term = "usb " * 50

    home_page = HomePage(page)
    results_page = SearchResultsPage(page)

    home_page.load(config.base_url)
    home_page.search_for(long_search_term)

    results_page.wait_until_loaded()
