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
    home_page = HomePage(page)
    results_page = SearchResultsPage(page)

    home_page.load(config.base_url)
    home_page.search_with_enter("gaming mouse")

    results_page.wait_until_loaded()
    results_page.results_list.expect_minimum_results(1)
