import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from pytest_bdd import given
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from Problem_2.actions.ui_actions import UiActions
from Problem_2.pages.home_page import HomePage
from Problem_2.pages.result_page import ResultPage
from Problem_2.test_data import TestData


@pytest.fixture
def browser():
    # Choose your browser here (Chrome/Firefox)
    browser_name = "chrome"

    if browser_name.lower() == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser_name.lower() == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1280")
        options.add_argument("--height=800")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    else:
        raise ValueError("Unsupported browser: " + browser_name)

    yield driver
    driver.close()
    driver.quit()


@pytest.fixture
def home_page(browser):
    return HomePage(browser)


@pytest.fixture
def result_page(browser):
    return ResultPage(browser)


@pytest.fixture
def ui_actions(browser):
    return UiActions(browser)


@given("I open the longest substring web page")
def navigate_home_page(browser):
    browser.get(TestData.home_page_url)
