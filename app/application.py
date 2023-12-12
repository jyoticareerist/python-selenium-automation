from pages.base_page import Page
from pages.main_page import MainPage
from pages.search_results import SearchResultsPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.product_details import ProductDetailsPage
from pages.circle_page import CirclePage
from pages.partner_page import PartnerPage
from pages.terms_and_conditions_page import TermsAndConditionsPage
from pages.help_page import HelpPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.login_page = LoginPage(driver)
        self.product_details_page = ProductDetailsPage(driver)
        self.partner_page = PartnerPage(driver)
        self.circle_page = CirclePage(driver)
        self.terms_and_conditions_page = TermsAndConditionsPage(driver)
        self.help_page = HelpPage(driver)
