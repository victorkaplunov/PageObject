from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        """Check login form presents."""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login name form is not present"

    def should_be_register_form(self):
        """Check register form presents."""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def register_new_user(self, email, password):
        """Register a new user"""
        link = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        link.send_keys(email)
        link = self.browser.find_element(*LoginPageLocators.NEW_PASSWORD_FIELD1)
        link.send_keys(password)
        link = self.browser.find_element(*LoginPageLocators.NEW_PASSWORD_FIELD2)
        link.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()
