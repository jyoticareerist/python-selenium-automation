from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify Target Circle page is opened')
def verify_target_circle_page_opened(context):
    page_url = context.driver.current_url
    assert '/circle' in page_url, "Target Circle URL is not correct"
    print("Target Circle page is opened successfully")
    # sleep(6)


@then('Verify {count} Benefits Boxes are present')
def verify_target_circle_page_opened(context, count):
    benefits_boxes = context.driver.find_elements(By.CSS_SELECTOR, ".styles__BenefitCard-sc-9mx6dj-2")
    benefits_boxes_count = len(benefits_boxes)
    number_count = int(count)
    assert benefits_boxes_count == number_count,\
        f"Expected {number_count} benefits boxes but found {benefits_boxes_count}"

