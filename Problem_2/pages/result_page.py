from selenium.webdriver.remote.webdriver import WebDriver

from Problem_2.constant_locator import ResultPageLocator as loc
from Problem_2.utils import util

class ResultPage:
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def result(self):
        return util.get_element(self.browser, loc.result_text)