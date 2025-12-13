"""
This edge test verifies that the search functionality
handles special characters without causing errors.
It validates system stability against uncommon input.
"""

import pytest

from src.core.config import config
from src.pages.home_page import HomePage
from src.pages.search_results_page import SearchResultsPage


@pytest.mark.edge
def test_search_with_special_characters(page):
    home_page = HomePage(page)
    results_page = SearchResultsPage(page)

    home_page.load(config.base_url)
    home_page.search_for("!!!@@@###")

    results_page.wait_until_loaded()
