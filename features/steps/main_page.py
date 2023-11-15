from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

TARGET_CIRCLE_SELECTOR = (By.CSS_SELECTOR, '[class*=UtilityHeaderLinksContainer] a[href="/circle"]')


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


@when('Click Target Circle in Topmost navigation')
def click_target_circle(context):
    target_link = context.driver.find_element(*TARGET_CIRCLE_SELECTOR)
    target_link.click()
    sleep(4)
