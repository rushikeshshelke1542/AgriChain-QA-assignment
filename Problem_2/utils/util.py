from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def get_element(browser, locator, by=By.XPATH, timeout=20):
    try:
        element = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((by, locator))
        )
        return element
    except TimeoutException:
        print(f"Timeout: Element '{locator}' was not visible after {timeout} seconds.")
        return None
