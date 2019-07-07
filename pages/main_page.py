from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        link.click()

    def should_be_login_link(self):
        assert self.browser.find_element(By.CSS_SELECTOR, '#login_link'), "Login page is not present"