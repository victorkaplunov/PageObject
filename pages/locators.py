"""Locators for Oscar Sandbox internet shop"""
from selenium.webdriver.common.by import By


class MainPageLocators:
    """locators for main page"""
    LOGIN_LINK = (By.CSS_SELECTOR, '#registration_link')


class LoginPageLocators:
    """locators for login/registration page"""
    LOGIN_PAGE_URL = '/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '#id_login-username')
    REGISTER_FORM = (By.CSS_SELECTOR, '#id_registration-email')


class ProductPageLocators:
    """locators for product page"""
    ADD_BOOK_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_DESCRIPTION = (By.ID, "product_description")
    BOOK_TITLE = (By.TAG_NAME, 'h1')
    MESSAGE_BOOK_TITLE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BOOK_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    MESSAGE_BOOK_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
