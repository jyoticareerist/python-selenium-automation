Feature: Lesson9 Classwork

  Scenario: User can see signin arrow
    Given Open target.com
    When Hover over signin
    Then Verify signin arrow shown

  Scenario Outline: User can select Help topic
    Given Open Help page for Returns
    Then Verify Returns page opened
    When Select Help topic <selected_help_topic>
    Then Verify <expected_page> page opened
    Examples:
    | selected_help_topic   | expected_page         |
    | Promotions & Coupons  | Current promotions    |
    | Holiday Help          | Holiday Help          |
    | Partner Programs      | Ulta Beauty at Target |
    | Target Account        | Create account        |
