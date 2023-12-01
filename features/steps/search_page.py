from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_ITEM_SELECTOR = (By.CSS_SELECTOR, ".styles__StyledCardWrapper-sc-z8946b-0 .styles__StyledLink-sc-vpsldm-0.styles__StyledTitleLink-sc-14ktig2-1")


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]').click()
    # sleep(6)


@then('Verify Search worked for {search_key}')
def verify_search(context, search_key):
    search_results_header = context.driver.find_element(By.CSS_SELECTOR, '[data-test="resultsHeading"] span.h-text-bs').text
    assert search_key in search_results_header, f"Expected text {search_key} not in {search_results_header}"


@then('Verify search result url has {search_key}')
def verify_search_url(context, search_key):
    assert search_key in context.driver.current_url,\
        f"Expected text {search_key} not in {context.driver.current_url}"


@then('Click First Item in search results')
def click_first_item(context):
    sleep(6)
    context.driver.execute_script("window.scrollBy(0,500)", "")
    # sleep(6)
    search_result_first = context.driver.find_element(*SEARCH_ITEM_SELECTOR)
    search_result_first.click()
