from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

TARGET_CIRCLE_SELECTOR = (By.CSS_SELECTOR, '[class*=UtilityHeaderLinksContainer] a[href="/circle"]')
SIGN_IN_MENU_BUTTON = (By.CSS_SELECTOR, 'a[data-test="accountNav-signIn"]')


@given('Open target.com')
def open_target(context):
    context.app.main_page.open_main()


@when('Click Cart Icon')
def click_cart_icon(context):
    context.app.main_page.click_cart_icon()


@when('Click Sign In')
def click_sign_in_main(context):
    sign_in_link = context.driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Account, sign in"]')
    sign_in_link.click()
    context.driver.wait.until(
        EC.visibility_of_element_located(SIGN_IN_MENU_BUTTON),
        "Sign-In button under side menu not loaded!"
    )


@when('Click Sign In under menu')
def click_sign_in_side_menu(context):
    button = context.driver.find_element(*SIGN_IN_MENU_BUTTON)
    button.click()


@when('Click Target Circle in Topmost navigation')
def click_target_circle(context):
    target_link = context.driver.find_element(*TARGET_CIRCLE_SELECTOR)
    target_link.click()
