"""Classes for cart page"""
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    """Methods for basket page"""
    def should_not_be_goods_in_basket(self):
        """Check basket for emptiness."""
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT), \
            "Basket is not empty."
