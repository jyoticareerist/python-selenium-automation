Feature: Tests for product page

  Scenario: User can select colors
    Given Open target product A-88062531 page
    Then Verify user can click through colors


  Scenario: User click selects the correct color
    Given Open target product A-88062531 page
    Then Verify the selected color is the one that the user clicked
