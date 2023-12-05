from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button[aria-label*="Add to cart for "]')
PRODUCT_TITLE_SELECTOR = (By.CSS_SELECTOR, "h1.styles__StyledHeading-sc-1xmf98v-0")
CART_ITEMS_SELECTOR = (By.CSS_SELECTOR, ".ModalDrawer h4.styles__StyledHeading-sc-1xmf98v-0")
COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")


@given('Open target product A-88062531 page')
def open_target(context):
    context.driver.get('https://www.target.com/p/A-88062531')
    sleep(10)


@then('Verify the selected color is the one that the user clicked')
def click_and_verify_selected_color(context):
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()
        expected_color = color.get_attribute("alt")
        selected_color = context.driver.find_element(*SELECTED_COLOR).text.split('\n')[1]
        assert selected_color in expected_color, f'{expected_color} was clicked but {selected_color} got selected'
        print(f'{expected_color} was clicked and {selected_color} is selected correctly')


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Black', 'Brown', 'Cream', 'Dark Gray', 'Green']
    actual_colors = []
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text.split('\n')[1].split(' - ')[0]
        actual_colors.append(selected_color)

    assert len(expected_colors) == len(actual_colors), f'Expected {expected_colors} did not match actual {actual_colors}'


@then('Verify Product Details Page is opened')
def verify_product_details_page_opened(context):
    # page_url = context.driver.current_url
    # assert "/p/" in page_url, "Product Details page not opened"
    context.driver.wait.until(EC.url_contains("/p/"), message="Product Details page not opened")
    print("Product Details page is successfully opened.")


@then('Click Add to Cart button')
def click_add_to_cart(context):
    sleep(6)
    context.driver.execute_script("window.scrollBy(0,600)", "")
    sleep(6)
    context.driver.execute_script("window.scrollBy(0,600)", "")
    # sleep(6)
    add_to_cart_button = context.driver.find_element(*ADD_TO_CART_BUTTON)
    context.product_title = add_to_cart_button.get_attribute("aria-label")
    add_to_cart_button.click()


@then('Verify Item is added successfully to the cart')
def verify_item_added(context):
    product_title = context.product_title
    cart_item_label = context.driver.find_element(*CART_ITEMS_SELECTOR).text
    assert cart_item_label in product_title, f"Expected {product_title} not matching {cart_item_label}"
