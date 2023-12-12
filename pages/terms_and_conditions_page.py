from selenium.webdriver.common.by import By
from pages.base_page import Page


class TermsAndConditionsPage(Page):
    PAGE_TITLE = (By.CSS_SELECTOR , 'h1[data-test="page-title"]')

    def verify_terms_and_conditions_page_opened(self):
        self.verify_partial_url('terms-conditions')
        self.verify_partial_match('Terms & Conditions', *self.PAGE_TITLE)
