from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import Page


class HelpPage(Page):
    HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    TOPIC_SELECTION = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    def open_help_returns(self):
        self.open_url('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def verify_returns_opened(self):
        self.wait_until_visible('RETURNS-HEADER', *self.HEADER_RETURNS)

    def select_topic(self, help_topic):
        topic_selection = self.find_element(*self.TOPIC_SELECTION)
        select = Select(topic_selection)
        select.select_by_value(help_topic)

    def verify_correct_page_opened(self, page_name):
        page_header_selector = (By.XPATH, f"//h1[text()=' {page_name}']")
        self.wait_until_visible('PROMOTIONS-HEADER', *page_header_selector)
