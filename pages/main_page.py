from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page


class MainPage(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]')
    CART_ICON = (By.CSS_SELECTOR, 'a[href*=cart]')
    SIGN_IN_MAIN = (By.CSS_SELECTOR, 'a[aria-label="Account, sign in"]')
    SIGN_IN_MENU_BUTTON = (By.CSS_SELECTOR, '#listaccountNav-signIn a')
    SIGN_IN_MAIN_ARROW = (By.CSS_SELECTOR, 'a[aria-label="Account, sign in"] > div > svg.expander')

    def open_main(self):
        self.open_url('https://www.target.com/')

    def open_login_page(self):
        self.open_url('https://www.target.com/login')

    def search(self, search_key):
        self.input(search_key, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def click_cart_icon(self):
        self.click(*self.CART_ICON)

    def click_sign_in_main(self):
        self.click(*self.SIGN_IN_MAIN)

    def click_sign_in_side_menu(self):
        self.wait_until_visible('SIGN-IN-LINK', *self.SIGN_IN_MENU_BUTTON)
        self.click(*self.SIGN_IN_MENU_BUTTON)

    def hover_signin(self):
        signin_btn = self.find_element(*self.SIGN_IN_MAIN)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(signin_btn)
        # actions.perform()
        ActionChains(self.driver).move_to_element(signin_btn).perform()

    def verify_signin_arrow_visible(self):
        self.wait_until_visible('SIGN-IN_MAIN_ARROW', *self.SIGN_IN_MAIN_ARROW)

