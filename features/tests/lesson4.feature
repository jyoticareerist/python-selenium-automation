Feature: Test Scenarios for target.com

  @smoke @search
  Scenario: User can search for coffee
    Given Open target.com
    When Search for coffee
    Then Verify Search worked for coffee
    And Verify search result url has coffee

  @smoke @search
  Scenario: User can search for toys for babies
    Given Open target.com
    When Search for toys for babies
    Then Verify Search worked for toys for babies
    And Verify search result url has toys+for+babies

  @smoke @search
  Scenario Outline: User can search for a product
    Given Open target.com
    When Search for <search_key>
    Then Verify Search worked for <expected_search_key>
    And Verify search result url has <expected_search_key_in_url>
    Examples:
    |search_key     |expected_search_key    |expected_search_key_in_url |
    |coffee         |coffee                 |coffee                     |
    |carpet         |carpet                 |carpet                     |
    |toys for babies|toys for babies        |toys+for+babies            |

  @smoke @search @cart
  Scenario: User searches for carpet, adds to cart and verifies successfully added to cart
    Given Open target.com
    When Search for carpet
    Then Verify Search worked for carpet
    And Verify search result url has carpet
    And Click First Item in search results
    And Verify Product Details Page is opened
    And Click Add to Cart button
    And Verify Item is added successfully to the cart
