"""Tests for product page"""
import pytest
from faker import Faker
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.cart_page import BasketPage


@pytest.mark.need_review
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                 marks=pytest.mark.xfail(reason="expected persistent bug")),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_cart(browser, link):
    """Go to page with promo 'newYear' and add book to basket.
    Compare title and price in message and book description."""

    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.compare_book_title(page.get_book_title_from_message())
    page.compare_book_price(page.get_book_price_from_message())


def test_guest_cant_see_success_message(browser):
    """Go to book page and check the success message presence."""

    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    """Go to book page and check the login link presence."""

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """Go to book page, click login link and check the URL of page. It must be login page"""

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_url()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    """Check emptiness of basket for fist guest visit."""

    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, link)
    page.should_not_be_goods_in_basket()
    page.basket_is_empty_message_present()


class TestUserAddToCartFromProductPage():
    """ Tests and setup for basket page."""
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        """Setup fixture for tests in this class. It is register new user."""

        fake = Faker()
        email = fake.email()
        password = fake.password(length=9)
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)

    def test_user_cant_see_success_message(self, browser):
        """Check if success message present on a book page."""

        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        """Go to page with promo 'newYear' and add book to basket.
        In alert window insert data. Compare title and price in message
        and book description. We are register a user before test."""

        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.compare_book_title(page.get_book_title_from_message())
        page.compare_book_price(page.get_book_price_from_message())
