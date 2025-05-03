from Problem_2.constant_locator import HomePageLocator as loc
from Problem_2.utils import util


class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def input_field(self):
        return util.get_element(self.browser, loc.input_field)

    def submit_button(self):
        return util.get_element(self.browser, loc.submit_button)
