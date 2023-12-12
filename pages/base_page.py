from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def wait_until_click(self, element_name, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            f'{element_name} not clickable!'
        )
        self.click(*locator)

    def wait_until_visible(self, element_name, *locator):
        print(f'{element_name} wait until visible')
        self.wait.until(
            EC.visibility_of_element_located(locator),
            f"{element_name} not present!"
        )

    def wait_for_url_to_change(self, initial_url):
        self.wait.until(
            EC.url_changes(initial_url),
            message=f'Url {initial_url} did not change'
        )

    def get_current_window(self):
        return self.driver.current_window_handle

    def get_all_windows(self):
        return self.driver.window_handles

    def switch_to_new_window(self):
        self.driver.wait.until(EC.new_window_is_opened)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    def switch_to_window(self, window_id):
        self.driver.switch_to.window(window_id)

    def close_page(self):
        self.driver.close()

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
