from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target.com')
def open_google(context):
    context.driver.get('https://www.target.com/')


@when('Click Cart Icon')
def click_cart_icon(context):
    cart_icon = context.driver.find_element(By.CSS_SELECTOR, 'a[href*=cart]')
    cart_icon.click()
    sleep(4)


@when('Click Sign In')
def click_sign_in_main(context):
    sign_in_link = context.driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Account, sign in"]')
    sign_in_link.click()
    sleep(4)


@when('Click Sign In under menu')
def click_sign_in_side_menu(context):
    button = context.driver.find_element(By.CSS_SELECTOR, 'a[data-test="accountNav-signIn"]')
    sleep(4)
    context.driver.execute_script("arguments[0].click();", button)
    sleep(4)


@then('Verify Cart is empty')
def verify_cart_is_empty(context):
    h1_element = context.driver.find_element(By.XPATH, '//h1[contains(text(), "Your cart is empty")]')
    assert h1_element is not None, "'Your cart is empty' message is not present"
    print("'Your cart is empty' message is present.")


@then('Verify Sign In form opened')
def verify_sign_in_form_opened(context):
    # Assert that the 'www.target.com/login' is present in the url.
    expected_in_url = "www.target.com/login"
    current_url = context.driver.current_url.lower()
    assert expected_in_url in current_url, f"1. Error: '{expected_in_url}' is not present in Current URL ({current_url})"
    print(f"1. '{expected_in_url}' is present in the Current URL")

    # wait for 4 sec
    sleep(4)

    # Assert that the 'Sign into your Target account' title message is present.
    expected_message = "Sign into your Target account"
    actual_message = context.driver.find_element(By.XPATH, '//span[contains(text(), "Sign into your Target account")]').text
    assert expected_message in actual_message, f"2. Error: expected_result ({expected_message}) not present in actual_result ({actual_message})"
    print(f"2. '{expected_message}' message is present on the page")

    # Assert that the 'Sign in' button is present.
    sign_in_button = context.driver.find_element(By.CSS_SELECTOR, "button#login[type='submit']")
    assert sign_in_button is not None, f"3. 'Sign In' button not present"
    print(f"3. 'Sign In' button is present in the sidebar form")
