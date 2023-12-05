Feature: Test Scenarios for target.com

  Scenario: click on the cart icon and verify that “Your cart is empty” message is shown
    Given Open target.com
    When Click Cart Icon
    Then Verify Cart is empty

  Scenario: verify that logged out user can Sign In successfully
    Given Open target.com
    When Click Sign In
    And Click Sign In under menu
    Then Verify Sign In page is opened
    And Verify Sign In form is opened
    And Input email and password on SignIn page
    And Click Sign In
    And Verify user is logged in (sign in form should disappear)

