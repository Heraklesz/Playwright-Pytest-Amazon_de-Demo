"""
This module represents the Amazon Cart page.
It encapsulates cart-level validations and actions such as
verifying cart state, checking item presence, and interacting
with basic cart controls.
The page object is primarily used in end-to-end and regression tests.
"""

from playwright.sync_api import Page, expect

from src.pages.base_page import BasePage


class CartPage(BasePage):
    """
    Page object for the Amazon shopping cart page.
    """

    CART_CONTAINER = "#sc-active-cart"
    CART_ITEMS = "div.sc-list-item"
    EMPTY_CART_MESSAGE = "div.sc-your-amazon-cart-is-empty"

    def __init__(self, page: Page):
        super().__init__(page)

    def wait_until_loaded(self) -> None:
        """
        Waits until the cart page is fully loaded.
        """
        self.page.wait_for_load_state("networkidle")
        expect(self.page.locator(self.CART_CONTAINER)).to_be_visible()

    def expect_cart_has_items(self) -> None:
        """
        Asserts that at least one item is present in the cart.
        """
        items = self.page.locator(self.CART_ITEMS)
        expect(items.first).to_be_visible()

    def expect_cart_is_empty(self) -> None:
        """
        Asserts that the cart is empty.
        """
        expect(self.page.locator(self.EMPTY_CART_MESSAGE)).to_be_visible()
