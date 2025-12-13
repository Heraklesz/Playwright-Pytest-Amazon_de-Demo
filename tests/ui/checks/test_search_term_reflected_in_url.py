"""
This check ensures that the searched term is reflected
in the resulting page URL.
It validates correct query propagation.
"""

import pytest

from src.core.config import config
from src.pages.home_page import HomePage
from src.pages.search_results_page import SearchResultsPage


@pytest.mark.checks
def test_search_term_is_reflected_in_url(page):
    search_term = "bluetooth speaker"

    home_page = HomePage(page)
    results_page = SearchResultsPage(page)

    home_page.load(config.base_url)
    home_page.search_for(search_term)

    results_page.wait_until_loaded()
    results_page.expect_search_term_in_url(search_term)
