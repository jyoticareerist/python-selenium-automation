from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@then('Verify Cart page is opened')
def verify_cart_page_opened(context):
    context.app.cart_page.verify_cart_page()


@then('Verify Cart is empty')
def verify_cart_is_empty(context):
    context.app.cart_page.verify_empty_cart()


# @then('Verify Item is added successfully to the cart')
# def verify_item_added(context):
#     context.app.cart_page.verify_item_added(context.product_title)
