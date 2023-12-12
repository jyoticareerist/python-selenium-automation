from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class CirclePage(Page):
    BENEFITS_BOXES = (By.CSS_SELECTOR, ".styles__BenefitCard-sc-9mx6dj-2")
    TABS = (By.CSS_SELECTOR, "[class*='PageSelectionText'] a")
    BONUS_TAB = (By.CSS_SELECTOR, "[data-test='bonus-tab']")
    GOOGLE_PLAY_BTN = (By.CSS_SELECTOR, "[alt='Get it on Google Play']")

    def verify_circle_page_opened(self):
        self.verify_partial_url('https://www.target.com/circle')

    def verify_benefits_boxes_present(self, count):
        benefits_boxes = self.driver.find_elements(*self.BENEFITS_BOXES)
        benefits_boxes_count = len(benefits_boxes)
        number_count = int(count)
        assert benefits_boxes_count == number_count,\
            f"Expected {number_count} benefits boxes but found {benefits_boxes_count}"

    def open_circle(self):
        self.open_url('https://www.target.com/circle')

    def click_google_play(self):
        self.click(*self.GOOGLE_PLAY_BTN)

    def verify_can_click_tabs(self):
        self.wait_until_visible('BONUS-TABS', *self.BONUS_TAB)
        tabs = self.find_elements(*self.TABS)

        current_url = ''
        for i in range(len(tabs)):
            self.find_elements(*self.TABS)[i].click()

            self.wait_for_url_to_change(current_url)
            current_url = self.driver.current_url
