from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UiActions:
    def __init__(self, browser: WebDriver):
        self.browser = browser

    @staticmethod
    def click_element(element):
        element.click()

    @staticmethod
    def send_text(element, text):
        element.clear()
        element.send_keys(text)

    @staticmethod
    def get_element_text(element):
        return element.text

    def get_all_window(self):
        return self.browser.window_handles

    def get_current_window(self):
        return self.browser.current_window_handle

    def switch_to_window(self, window):
        self.browser.switch_to.window(window)

    def wait_till_new_window_loads(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.number_of_windows_to_be(2))

    def get_window_url(self):
        return self.browser.current_url
