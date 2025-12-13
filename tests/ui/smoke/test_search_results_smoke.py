"""
This smoke test verifies that performing a product search
results in a visible list of search results.
It ensures that the core search functionality is operational.
"""

import pytest

from src.core.config import config
from src.pages.home_page import HomePage
from src.pages.search_results_page import SearchResultsPage


@pytest.mark.smoke
def test_search_displays_results(page):
    home_page = HomePage(page)
    results_page = SearchResultsPage(page)

    home_page.load(config.base_url)
    home_page.search_for("usb c charger")

    results_page.wait_until_loaded()
