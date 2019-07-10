"""Locators for Oscar Sandbox internet shop"""
from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.ID, "registration_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR,
                   '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    """locators for main page"""
    LOGIN_LINK = (By.CSS_SELECTOR, '#registration_link')


class LoginPageLocators:
    """locators for login/registration page"""
    LOGIN_PAGE_URL = '/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '#id_login-username')
    REGISTER_FORM = (By.CSS_SELECTOR, '#id_registration-email')
    NEW_PASSWORD_FIELD1 = (By.ID, 'id_registration-password1')
    NEW_PASSWORD_FIELD2 = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators:
    """locators for product page"""
    ADD_BOOK_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_DESCRIPTION = (By.ID, "product_description")
    BOOK_TITLE = (By.TAG_NAME, 'h1')
    MESSAGE_BOOK_TITLE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    BOOK_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    MESSAGE_BOOK_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div')


class BasketPageLocators:
    """locators for product page"""
    BASKET_CONTENT = (By.CSS_SELECTOR, '#basket_formset > div')
    BASKET_IS_EMPTY_MESSAGE = (By.XPATH, '//*[@id="content_inner"]/p')
