from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_ITEM_SELECTOR = (By.CSS_SELECTOR, ".styles__StyledCardWrapper-sc-z8946b-0 .styles__StyledLink-sc-vpsldm-0.styles__StyledTitleLink-sc-14ktig2-1")
SEARCH_ITEM_SELECTOR_2 = (By.CSS_SELECTOR, "styles__StyledCardWrapper-sc-z8946b-0.kBCbIH.h-padding-a-tight")
SEARCH_FIELD = (By.ID, 'search')


@when('Search for {product}')
def search_product(context, product):
    context.app.main_page.search(product)


@then('Verify Search worked for {search_key}')
def verify_search(context, search_key):
    context.app.search_results_page.verify_search_result(search_key)


@then('Verify search result url has {search_key}')
def verify_search_url(context, search_key):
    context.app.search_results_page.verify_search_url(search_key)


@then('Click First Item in search results')
def click_first_item(context):
    context.app.search_results_page.click_first_item()


@then('Verify each search result product has Image and Title')
def verify_each_item(context):
    context.app.search_results_page.verify_each_item()