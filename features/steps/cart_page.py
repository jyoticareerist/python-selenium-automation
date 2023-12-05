from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@then('Verify Cart page is opened')
def verify_cart_page_opened(context):
    # page_url = context.driver.current_url
    # assert "/cart" in page_url, "Cart page not opened"
    context.driver.wait.until(EC.url_contains("/cart"), message="Cart page not opened")
    print("Cart page is successfully opened.")


@then('Verify Cart is empty')
def verify_cart_is_empty(context):
    # h1_element = context.driver.find_element(By.XPATH, '//h1[contains(text(), "Your cart is empty")]')
    # assert h1_element is not None, "'Your cart is empty' message is not present"
    # print("'Your cart is empty' message is present.")
    context.app.cart_page.verify_empty_cart()
