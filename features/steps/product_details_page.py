from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button[aria-label*="Add to cart for "]')
PRODUCT_TITLE_SELECTOR = (By.CSS_SELECTOR, "h1.styles__StyledHeading-sc-1xmf98v-0")
CART_ITEMS_SELECTOR = (By.CSS_SELECTOR, ".ModalDrawer h4.styles__StyledHeading-sc-1xmf98v-0")


@then('Verify Product Details Page is opened')
def verify_product_details_page_opened(context):
    page_url = context.driver.current_url
    assert "/p/" in page_url, "Product Details page not opened"
    print("Product Details page is successfully opened.")


@then('Click Add to Cart button')
def click_add_to_cart(context):
    sleep(6)
    context.driver.execute_script("window.scrollBy(0,500)", "")
    sleep(6)
    add_to_cart_button = context.driver.find_element(*ADD_TO_CART_BUTTON)
    add_to_cart_button.click()


@then('Verify Item is added successfully to the cart')
def verify_item_added(context):
    product_title = context.driver.find_element(*ADD_TO_CART_BUTTON).get_attribute("aria-label")
    cart_item_label = context.driver.find_element(*CART_ITEMS_SELECTOR).text
    assert cart_item_label in product_title, f"Expected {product_title} not matching {cart_item_label}"
