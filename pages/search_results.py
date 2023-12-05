from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT_HEADING = (By.CSS_SELECTOR, '[data-test="resultsHeading"] span.h-text-bs')
    SEARCH_ITEM_SELECTOR = (By.CSS_SELECTOR,
                            ".styles__StyledCardWrapper-sc-z8946b-0 .styles__StyledLink-sc-vpsldm-0.styles__StyledTitleLink-sc-14ktig2-1")
    SEARCH_ITEM_SELECTOR_2 = (By.CSS_SELECTOR, "styles__StyledCardWrapper-sc-z8946b-0.kBCbIH.h-padding-a-tight")

    def verify_search_url(self, search_key):
        self.verify_partial_url(search_key)

    def verify_search_result(self, search_key):
        self.verify_partial_match(search_key, *self.SEARCH_RESULT_HEADING)

    def click_first_item(self):
        self.scroll()
        self.click(*self.SEARCH_ITEM_SELECTOR)

    def verify_each_item(self):
        self.scroll()
        search_results = self.find_elements(*self.SEARCH_ITEM_SELECTOR_2)
        for product in search_results:
            product_title = product.find_element(By.CSS_SELECTOR, '[data-test="product-title"]').text
            assert product_title, "Product Title not found"
            product_img = product.find_element(By.CSS_SELECTOR, 'img')
            assert product_img, "Product Image not found"
