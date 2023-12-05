from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]')
    CART_EMPTY_TITLE = (By.XPATH, '//h1[contains(text(), "Your cart is empty")]')

    def verify_empty_cart(self):
        h1_element = self.find_element(*self.CART_EMPTY_TITLE)
        assert h1_element is not None, "'Your cart is empty' message is not present"
        print("'Your cart is empty' message is present.")
