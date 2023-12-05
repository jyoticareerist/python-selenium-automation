from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class LoginPage(Page):
    TITLE_MESSAGE = (By.CSS_SELECTOR, '.styles__StyledHeading-sc-1xmf98v-0.styles__AuthHeading-sc-kz6dq2-2')
    SIGNIN_BTN = (By.CSS_SELECTOR, "button#login[type='submit']")
    EMAIL_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    SIGNIN_BTN_TEXT = 'Sign-In button'
    EMAIL_FIELD_TEXT = 'Email Field'
    PASSWORD_FIELD_TEXT = 'Password Field'

    def verify_login_page(self):
        self.verify_partial_url('login')

    def verify_title_present(self):
        self.verify_exact_match('Sign into your Target account', *self.TITLE_MESSAGE)

    def verify_signin_button_present(self):
        self.verify_element_present('Sign-In button', *self.SIGNIN_BTN)

    def verify_signin_form_opened(self):
        self.verify_title_present()
        self.verify_signin_button_present()

    def input_email_password(self):
        self.input('****@*****.***', *self.EMAIL_FIELD)
        self.input('*****', *self.PASSWORD_FIELD)

    def click_sign_in(self):
        self.wait_until_click(self.SIGNIN_BTN_TEXT, *self.SIGNIN_BTN)

    def verify_signin_success(self):
        sleep(30)
        self.verify_element_disappears(self.EMAIL_FIELD_TEXT, *self.EMAIL_FIELD)
        self.verify_element_disappears(self.PASSWORD_FIELD_TEXT, *self.PASSWORD_FIELD)
        self.verify_element_disappears(self.SIGNIN_BTN_TEXT, *self.SIGNIN_BTN)
        self.verify_partial_url('login')