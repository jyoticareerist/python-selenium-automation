Feature: Test Scenarios for target.com

  @smoke @cart
  Scenario: click on the cart icon and verify that “Your cart is empty” message is shown
    Given Open target.com
    When Click Cart Icon
    Then Verify Cart is empty

  @login
  Scenario: verify that logged out user can Sign In successfully
    Given Open target.com
    When Click Sign In
    And Click Sign In under menu
    Then Verify Sign In page is opened
    And Verify Sign In form is opened
    And Input email (abcd@xyz.com) and password (some-password) on SignIn page
    And Click Sign In
    And Verify user is logged in (sign in form should disappear)

