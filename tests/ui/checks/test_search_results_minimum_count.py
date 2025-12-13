"""
This check validates that a product search returns
at least one visible result item.
It serves as a generic site health verification.
"""

import pytest

from src.core.config import config
from src.pages.home_page import HomePage
from src.pages.search_results_page import SearchResultsPage


@pytest.mark.checks
def test_search_returns_at_least_one_result(page):
    home_page = HomePage(page)
    results_page = SearchResultsPage(page)

    home_page.load(config.base_url)
    home_page.search_for("laptop stand")

    results_page.wait_until_loaded()
    results_page.results_list.expect_minimum_results(1)
