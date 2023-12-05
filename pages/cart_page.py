from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_TITLE = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")

    def verify_cart_page(self):
        self.verify_partial_url('cart')

    def verify_empty_cart(self):
        self.verify_exact_match('Your cart is empty', *self.CART_EMPTY_TITLE)

