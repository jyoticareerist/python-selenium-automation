from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify Sign In page is opened')
def verify_signin_page_opened(context):
    # Assert that the 'www.target.com/login' is present in the url.
    expected_in_url = "www.target.com/login"
    current_url = context.driver.current_url.lower()
    assert expected_in_url in current_url, f"1. Error: '{expected_in_url}' is not present in Current URL ({current_url})"
    print(f"1. '{expected_in_url}' is present in the Current URL")

    # wait for 4 sec
    sleep(4)


@then('Verify Title is present')
def verify_title_present(context):
    # Assert that the 'Sign into your Target account' title message is present.
    expected_message = "Sign into your Target account"
    actual_message = context.driver.find_element(By.XPATH, '//span[contains(text(), "Sign into your Target account")]').text
    assert expected_message in actual_message, f"2. Error: expected_result ({expected_message}) not present in actual_result ({actual_message})"
    print(f"2. '{expected_message}' message is present on the page")


@then('Verify SignIn button is present')
def verify_signin_button_present(context):
    sign_in_button = context.driver.find_element(By.CSS_SELECTOR, "button#login[type='submit']")
    assert sign_in_button is not None, f"3. 'Sign In' button not present"
    print(f"3. 'Sign In' button is present in the sidebar form")
