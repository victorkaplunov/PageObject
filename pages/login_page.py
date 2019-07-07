from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        # self.should_be_login_form()
        # self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        # print(LoginPageLocators.LOGIN_PAGE_URL)
        print("Assert: ", self.is_string_in_url_present(LoginPageLocators.LOGIN_PAGE_URL))
        assert self.is_string_in_url_present(LoginPageLocators.LOGIN_PAGE_URL), "URL do not contain 'login' string."

    # def should_be_login_form(self):
    #     # реализуйте проверку, что есть форма логина
    #     assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login name form is not present"
    #
    # def should_be_register_form(self):
    #     # реализуйте проверку, что есть форма регистрации на странице
    #     assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register e-mail form is not present"
