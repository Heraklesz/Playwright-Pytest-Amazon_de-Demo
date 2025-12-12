"""
This module defines a reusable page component responsible for handling
the cookie consent banner on Amazon pages.
It encapsulates logic for detecting and accepting cookies to keep
tests clean and free from repetitive consent-handling code.
"""
from playwright.sync_api import Page, expect

class CookieBanner:
    """
    Represents the cookie consent banner component.
    """

    ACCEPT_BUTTON = "button#sp-cc-accept"

    def __init__(self, page: Page):
        self.page = page

    def accept_cookies_if_present(self) -> None:
        """
        Accepts cookies if the banner is visible.
        Safely does nothing if the banner is not present.
        """
        banner_button = self.page.locator(self.ACCEPT_BUTTON)
        if banner_button.is_visible():
            expect(banner_button).to_be_enabled()
            banner_button.click()
