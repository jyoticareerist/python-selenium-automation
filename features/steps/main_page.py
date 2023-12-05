from selenium.webdriver.common.by import By
from behave import given, when, then

TARGET_CIRCLE_SELECTOR = (By.CSS_SELECTOR, '[class*=UtilityHeaderLinksContainer] a[href="/circle"]')
SIGN_IN_MENU_BUTTON = (By.CSS_SELECTOR, 'a[data-test="accountNav-signIn"]')


@given('Open target.com')
def open_target(context):
    context.app.main_page.open_main()


@when('Click Cart Icon')
def click_cart_icon(context):
    context.app.main_page.click_cart_icon()


@then('Navigate to Cart Page')
def navigate_cart_page(context):
    context.app.main_page.click_cart_icon()


@when('Click Sign In')
def click_sign_in_main(context):
    context.app.main_page.click_sign_in_main()
    context.app.page.wait_until_visible(SIGN_IN_MENU_BUTTON)


@when('Click Sign In under menu')
def click_sign_in_side_menu(context):
    context.app.main_page.click_sign_in_side_menu()


@when('Click Target Circle in Topmost navigation')
def click_target_circle(context):
    context.app.click(*TARGET_CIRCLE_SELECTOR)
