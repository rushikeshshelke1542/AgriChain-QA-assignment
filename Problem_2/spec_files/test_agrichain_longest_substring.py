import os

from pytest_bdd import scenario, given, when, then
from pytest_bdd import parsers

Feature_file = os.getcwd() + "/features/test_agrichain_longest_substring.feature"

from pytest_bdd import scenario, when, then, parsers


@scenario(Feature_file, "Enter a string with repeating characters")
def test_longest_substring_without_repeating_character():
    """BDD Scenario: Validate longest substring without repeating characters."""
    pass


@when(parsers.parse('I enter the {string}'))
def enter_text(ui_actions, home_page, string):
    """
    Step to enter a string in the input field.

    Args:
        ui_actions: Utility class for UI interactions.
        home_page: Page object representing the input screen.
        string (str): The string entered by the user in the test.
    """
    ui_actions.send_text(home_page.input_field(), string)


@when("I click on the submit button")
def click_submit_button(ui_actions, home_page):
    """
    Step to click the submit button and wait for the new window to load.

    Args:
        ui_actions: Utility class for UI interactions.
        home_page: Page object representing the input screen.
    """
    ui_actions.click_element(home_page.submit_button())
    ui_actions.wait_till_new_window_loads()


@when("I switch to the new window")
def switch_new_window(ui_actions):
    """
    Step to switch WebDriver context to the newly opened window.

    Args:
        ui_actions: Utility class for UI interactions.
    """
    original_window = ui_actions.get_current_window()

    all_windows = ui_actions.get_all_window()
    for handle in all_windows:
        if handle != original_window:
            ui_actions.switch_to_window(handle)
            break


@then(parsers.parse("I should see the {result}"))
def verify_result(ui_actions, result_page, result):
    """
    Step to verify the longest unique substring shown in the result window.

    Args:
        ui_actions: Utility class for UI interactions.
        result_page: Page object for the result view.
        result (str): Expected result string.
    """
    actual_result = ui_actions.get_element_text(result_page.result())
    assert actual_result == result, f"Expected {result}, but got {actual_result}"
