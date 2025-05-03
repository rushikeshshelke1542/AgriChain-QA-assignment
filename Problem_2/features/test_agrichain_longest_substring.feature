Feature: Longest Substring Without Repeating Characters
  As a user
  I want to enter a string and find the longest substring without repeating characters
  So that I can see the result displayed on the new tab after user clicks submit

  Background: Navigate to home page
    Given I open the longest substring web page

  #combined all the 3 test case in single test case with multiple inputs

  Scenario Outline: Enter a string with repeating characters
    When I enter the <string>
    And I click on the submit button
    And I switch to the new window
    Then I should see the <result>

    Examples:
      |string| result |
      |abcabcbb | abc |
      |  aaaaa   |a|
      |  abcdef       |abcdef |


  Scenario: Enter a string with all unique characters
    When I enter the string "abcdef"
    And I click on the submit button
    And I switch to the new window
    Then I should see the result "abcdef"

  Scenario: Enter a string with all identical characters
    When I enter the string "aaaaa"
    And I click on the submit button
    And I switch to the new window
    Then I should see the result "a"

  Scenario: Submit button is disabled until text is entered
    When I do not enter any text in the input field
    Then the Submit button should be disabled

