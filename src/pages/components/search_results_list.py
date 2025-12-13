"""
This module defines a reusable component representing the list of search results.
It encapsulates logic related to locating and validating product result items
on the Amazon search results page.
The component is designed to be used by the SearchResultsPage object.
"""
from playwright.sync_api import Page, Locator, expect


class SearchResultsList:
    """
    Represents the product results list on the search results page.
    """

    RESULT_ITEMS = "div[data-component-type='s-search-result']"

    def __init__(self, page: Page):
        self.page = page
        self.items: Locator = page.locator(self.RESULT_ITEMS)

    def wait_until_loaded(self) -> None:
        """
        Waits until at least one search result item is visible.
        """
        expect(self.items.first).to_be_visible()

    def get_results_count(self) -> int:
        """
        Returns the number of visible search result items.
        """
        return self.items.count()

    def expect_minimum_results(self, minimum: int = 1) -> None:
        """
        Asserts that at least a given number of results are displayed.
        """
        assert self.get_results_count() >= minimum
