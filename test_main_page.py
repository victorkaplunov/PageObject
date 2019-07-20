"""Tests for main page"""
from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.cart_page import BasketPage


def test_guest_can_go_to_login_page(browser):
    """Check if guest can go to registration page from promo page."""

    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page = BasePage(browser, link)
    page.go_to_registration_page()


def test_guest_should_see_login_link(browser):
    """Check if guest can see login link from promo page."""

    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    page = BasePage(browser, link)
    page.should_be_registration_link()


def test_guest_should_be_at_login_page(browser):
    """Check login page URL for unauthorized users. Check presence of login and register form at this page."""

    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    """Check if guest can go to basket. Check if guest can see only empty basket at first visit."""

    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, link)
    page.should_not_be_goods_in_basket()
    page.basket_is_empty_message_present()
