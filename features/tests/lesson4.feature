Feature: Test Scenarios for target.com

  Scenario: User can search for coffee
    Given Open target.com
    When Search for coffee
    Then Verify Search worked for coffee
    And Verify search result url has coffee

  Scenario: User can search for toys
    Given Open target.com
    When Search for toys
    Then Verify Search worked for toys
    And Verify search result url has toys

  Scenario: User can search for gifts for women
    Given Open target.com
    When Search for gifts for women
    Then Verify Search worked for gifts for women
    And Verify search result url has gifts+for+women

  Scenario Outline: User can search for a product
    Given Open target.com
    When Search for <search_key>
    Then Verify Search worked for <expected_search_key>
    And Verify search result url has <expected_search_key_in_url>
    Examples:
    |search_key   |expected_search_key    |expected_search_key_in_url |
    |coffee       |coffee                 |coffee                     |
    |carpet       |carpet                 |carpet                     |
    |gifts for men|gifts for men          |gifts+for+men              |

  Scenario: Verify 5 benefits boxes on Target Circle
    Given Open target.com
    When Click Target Circle in Topmost navigation
    Then Verify Target Circle page is opened
    And Verify 5 Benefits Boxes are present

  Scenario: User searches for coffee, adds to cart and verifies successfully added to cart
    Given Open target.com
    When Search for coffee
    Then Verify Search worked for coffee
    And Verify search result url has coffee
    And Click First Item in search results
    And Verify Product Details Page is opened
    And Click Add to Cart button
    And Verify Item is added successfully to the cart
