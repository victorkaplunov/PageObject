"""Classes for product page"""
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException

class ProductPage(BasePage):
    """Methods for product page"""
    def add_to_basket(self):
        """Add book to basket"""
        link = self.browser.find_element(*ProductPageLocators.ADD_BOOK_TO_BASKET_BUTTON)
        link.click()

    def should_be_product_description(self):
        """Page must contain product description"""
        try:
            self.browser.find_element(*ProductPageLocators.PRODUCT_DESCRIPTION)
        except NoSuchElementException:
            return False
        return True

    def get_book_title_from_message(self):
        """Get book title from message"""
        print("Message: ", self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_TITLE).text)
        return self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_TITLE).text

    def get_book_price_from_message(self):
        """Get book title from message"""
        print("Message: ", self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_PRICE).text)
        return self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_PRICE).text

    def compare_book_title(self, title):
        """Compare name from text and message"""
        print("Body: ", self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text)
        return  self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text == title

    def compare_book_price(self, price):
        """Compare name from text and message"""
        print("Body: ", self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text)
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text == price
