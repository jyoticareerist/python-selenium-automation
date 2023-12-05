from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULT_HEADING = (By.CSS_SELECTOR, '[data-test="resultsHeading"] span.h-text-bs')

    def verify_search_url(self, search_key):
        assert search_key in self.driver.current_url, \
            f"Expected text {search_key} not in {self.driver.current_url}"

    def verify_search_result(self, search_key):
        search_results_header = self.find_element(*self.SEARCH_RESULT_HEADING).text
        assert search_key in search_results_header, f"Expected text {search_key} not in {search_results_header}"

