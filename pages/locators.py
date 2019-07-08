from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#registration_link')


class LoginPageLocators:
    LOGIN_PAGE_URL = '/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '#id_login-username')
    REGISTER_FORM = (By.CSS_SELECTOR, '#id_registration-email')
    
