from selenium.webdriver.common.by import By

from behave import given, when, then


@then('Verify Target Circle page is opened')
def verify_target_circle_page_opened(context):
    context.app.circle_page.verify_circle_page_opened()


@given('Open Circle page')
def open_circle(context):
    context.app.circle_page.open_circle()


@given('Store original window')
def store_windows(context):
    context.windows = context.app.page.get_all_windows()
    context.original_window = context.app.page.get_current_window()


@when('Click Google Play button')
def click_google_play(context):
    context.app.circle_page.click_google_play()


@when('Switch to new window')
def switch_window(context):
    context.app.page.switch_to_new_window()


@then('Verify {count} Benefits Boxes are present')
def verify_benefits_boxes_present(context, count):
    context.app.circle_page.verify_benefits_boxes_present(count)


@then('Verify that clicking though Circle tabs works')
def verify_can_click_tabs(context):
    context.app.circle_page.verify_can_click_tabs()


@then('Verify Google Play Target page opened')
def verify_google_play_opened(context):
    context.app.partner_page.verify_google_play_opened()


@then('Close current page')
def close(context):
    context.app.page.close_page()


@then('Return to original window')
def switch_to_original(context):
    context.app.page.switch_to_window(context.original_window)
