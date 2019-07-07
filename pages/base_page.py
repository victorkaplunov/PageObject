from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_string_in_url_present(self, url_substring):
        print(self.browser.current_url)
        print("Подстрока в URL? ", url_substring in self.browser.current_url)
        # url_substring in self.browser.current_url
        try:
            url_substring in self.browser.current_url
        except NoSuchElementException:
            return False
        return True
