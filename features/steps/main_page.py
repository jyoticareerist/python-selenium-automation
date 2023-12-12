from selenium.webdriver.common.by import By
from behave import given, when, then

TARGET_CIRCLE_SELECTOR = (By.CSS_SELECTOR, '[class*=UtilityHeaderLinksContainer] a[href="/circle"]')


@given('Open target.com')
def open_target(context):
    context.app.main_page.open_main()


@given('Open sign in page')
def open_login_page(context):
    context.app.main_page.open_main()
    context.app.main_page.click_sign_in_main()
    context.app.main_page.click_sign_in_side_menu()


@when('Click Cart Icon')
def click_cart_icon(context):
    context.app.main_page.click_cart_icon()


@when('Hover over signin')
def hover_signin(context):
    context.app.main_page.hover_signin()


@then('Verify signin arrow shown')
def verify_signin_arrow(context):
    context.app.main_page.verify_signin_arrow_visible()


@then('Navigate to Cart Page')
def navigate_cart_page(context):
    context.app.main_page.click_cart_icon()


@when('Click Sign In')
def click_sign_in_main(context):
    context.app.main_page.click_sign_in_main()


@when('Click Sign In under menu')
def click_sign_in_side_menu(context):
    context.app.main_page.click_sign_in_side_menu()


@when('Click Target Circle in Topmost navigation')
def click_target_circle(context):
    context.app.main_page.click(*TARGET_CIRCLE_SELECTOR)
