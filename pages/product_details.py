from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class ProductDetailsPage(Page):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.styles__ThreeUpButtonWrapper-sc-11rka0i-0 button[aria-label*="Add to cart for "]')
    CART_ITEM_H4 = (By.CSS_SELECTOR, ".h-padding-l-tight h4")

    def verify_product_details_page(self):
        self.verify_partial_url('/p/')

    def add_to_cart(self):
        self.scroll()
        sleep(10)
        add_to_cart_button = self.find_element(*self.ADD_TO_CART_BUTTON)
        product_title = add_to_cart_button.get_attribute("aria-label").replace("Add to cart for ", "")
        add_to_cart_button.click()
        return product_title

    def verify_item_added(self, product_title):
        self.verify_exact_match(product_title, *self.CART_ITEM_H4)
