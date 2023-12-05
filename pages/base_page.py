from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Page:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def wait_until_click(self, element_name, *locator):
        self.driver.wait.until(
            EC.element_to_be_clickable(locator),
            f'{element_name} not clickable!'
        )
        self.click(*locator)

    def wait_until_visible(self, element_name, *locator):
        self.driver.wait.until(
            EC.visibility_of_element_located(locator),
            f"{element_name} not present!"
        )

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_partial_match(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, \
            f'Expected({expected_text}) is not present in Actual({actual_text})'

    def verify_exact_match(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, \
            f'Expected({expected_text}) is not equal to Actual({actual_text})'

    def verify_partial_url(self, expected_url):
        current_url = self.get_current_url()
        self.driver.wait.until(
            EC.url_contains(expected_url),
            message=f'Expected Text ({expected_url}) not present in Actual URL({current_url})'
        )

    def verify_element_present(self, element_name, *locator):
        self.driver.wait.until(
            EC.visibility_of_element_located(locator),
            f'{element_name} not present!'
        )

    def verify_element_disappears(self, element_name, *locator):
        self.driver.wait.until(
            EC.invisibility_of_element_located(locator),
            f'{element_name} still present!'
        )

    def scroll(self):
        sleep(6)
        self.driver.execute_script("window.scrollBy(0,600)", "")
