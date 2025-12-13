"""
This module represents the Amazon Product Details Page (PDP).
It encapsulates product-level information and actions such as
verifying page load state and adding a product to the shopping cart.
This page object is primarily used in end-to-end user journeys.
"""

from playwright.sync_api import Page, expect

from src.pages.base_page import BasePage


class ProductPage(BasePage):
    """
    Page object for the Amazon product details page.
    """

    PRODUCT_TITLE = "#productTitle"
    ADD_TO_CART_BUTTON = "#add-to-cart-button"

    def __init__(self, page: Page):
        super().__init__(page)

    def wait_until_loaded(self) -> None:
        """
        Waits until the product title is visible,
        indicating that the PDP has fully loaded.
        """
        expect(self.page.locator(self.PRODUCT_TITLE)).to_be_visible()

    def add_product_to_cart(self) -> None:
        """
        Adds the current product to the shopping cart.
        """
        expect(self.page.locator(self.ADD_TO_CART_BUTTON)).to_be_visible()
        self.page.locator(self.ADD_TO_CART_BUTTON).click()
