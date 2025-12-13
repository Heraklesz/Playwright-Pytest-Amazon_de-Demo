"""
This module represents the Amazon search results page.
It provides high-level assertions and interactions related to search outcomes,
and composes the SearchResultsList component for result-specific logic.
Tests should rely on this abstraction instead of direct page interactions.
"""

from playwright.sync_api import Page, expect

from src.pages.base_page import BasePage
from src.pages.components.search_results_list import SearchResultsList


class SearchResultsPage(BasePage):
    """
    Page object for the Amazon search results page.
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.results_list = SearchResultsList(page)

    def wait_until_loaded(self) -> None:
        """
        Waits until the search results page is fully loaded.
        """
        self.page.wait_for_load_state("networkidle")
        self.results_list.wait_until_loaded()

    def expect_search_term_in_url(self, term: str) -> None:
        """
        Asserts that the searched term is reflected in the URL.
        """
        normalized = term.replace(" ", "+")
        assert f"s?k={normalized}" in self.page.url
