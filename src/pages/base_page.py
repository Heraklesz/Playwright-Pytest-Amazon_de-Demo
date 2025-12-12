"""
This module defines the BasePage class used as the foundation for all page objects.
It provides common browser interaction helpers such as safe clicking, filling inputs,
navigation, and basic assertions that improve test stability.
All concrete page objects should inherit from this class.
"""

from playwright.sync_api import Page, expect


class BasePage:
    """
    Base class for all page objects.
    Encapsulates common Playwright interactions and best practices.
    """

    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str) -> None:
        """
        Navigates to the given URL and waits until the page is fully loaded.
        """
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    def safe_click(self, locator: str) -> None:
        """
        Clicks an element after ensuring it is visible and enabled.
        """
        element = self.page.locator(locator)
        expect(element).to_be_visible()
        element.click()

    def safe_fill(self, locator: str, value: str) -> None:
        """
        Fills an input field after ensuring it is visible.
        """
        element = self.page.locator(locator)
        expect(element).to_be_visible()
        element.fill(value)

    def expect_visible(self, locator: str) -> None:
        """
        Asserts that an element is visible on the page.
        """
        expect(self.page.locator(locator)).to_be_visible()
