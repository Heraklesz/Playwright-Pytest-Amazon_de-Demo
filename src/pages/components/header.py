"""
This module defines a reusable Header component representing the global site header.
It encapsulates common header elements such as the logo, search bar, and cart icon.
The component is designed to be reused across multiple page objects and checks.
"""

from playwright.sync_api import Page, expect


class Header:
    """
    Represents the global Amazon header component.
    """

    LOGO = "#nav-logo-sprites"
    SEARCH_INPUT = "input#twotabsearchtextbox"
    SEARCH_SUBMIT = "input#nav-search-submit-button"
    CART_ICON = "#nav-cart"

    def __init__(self, page: Page):
        self.page = page

    def expect_logo_visible(self) -> None:
        """
        Asserts that the Amazon logo is visible in the header.
        """
        expect(self.page.locator(self.LOGO)).to_be_visible()

    def expect_search_bar_visible(self) -> None:
        """
        Asserts that the search input field is visible in the header.
        """
        expect(self.page.locator(self.SEARCH_INPUT)).to_be_visible()

    def expect_cart_icon_visible(self) -> None:
        """
        Asserts that the cart icon is visible in the header.
        """
        expect(self.page.locator(self.CART_ICON)).to_be_visible()
