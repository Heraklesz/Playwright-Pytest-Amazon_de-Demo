"""
This module represents the Amazon home page.
It provides high-level actions related to search and initial page interactions,
and composes reusable components such as the cookie banner.
Tests should interact with the home page only through this abstraction.
"""

from playwright.sync_api import Page

from src.pages.base_page import BasePage
from src.pages.components.cookie_banner import CookieBanner


class HomePage(BasePage):
    """
    Page object for the Amazon home page.
    """

    SEARCH_INPUT = "input#twotabsearchtextbox"
    SEARCH_SUBMIT = "input#nav-search-submit-button"

    def __init__(self, page: Page):
        super().__init__(page)
        self.cookie_banner = CookieBanner(page)

    def load(self, base_url: str) -> None:
        """
        Opens the Amazon home page and handles cookie consent if required.
        """
        self.goto(base_url)
        self.cookie_banner.accept_cookies_if_present()

    def search_for(self, term: str) -> None:
        """
        Performs a product search using the search submit button.
        """
        self.safe_fill(self.SEARCH_INPUT, term)
        self.safe_click(self.SEARCH_SUBMIT)

    def search_with_enter(self, term: str) -> None:
        """
        Performs a product search using the ENTER key.
        """
        self.safe_fill(self.SEARCH_INPUT, term)
        self.page.keyboard.press("Enter")
