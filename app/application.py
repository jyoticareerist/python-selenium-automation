from pages.base_page import Page
from pages.main_page import MainPage
from pages.search_results import SearchResultsPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.product_details import ProductDetailsPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.login_page = LoginPage(driver)
        self.product_details_page = ProductDetailsPage(driver)
