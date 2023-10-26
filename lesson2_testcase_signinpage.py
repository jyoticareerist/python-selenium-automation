from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# Click 'Orders' in Top Navigation to reach 'Sign In' page.
driver.find_element(By.ID, 'nav-orders').click()

# Assert that the 'www.amazon.com/ap/signin?' is present in the url.
expected_in_url = "www.amazon.com/ap/signin?"
current_url = driver.current_url.lower()

assert expected_in_url in current_url, f"Error: '{expected_in_url}' is not present in Current URL ({current_url})"

print(f"1. '{expected_in_url}' is present in the Current URL")

# Assert that the 'Sign in' h1 tag is present.
expected_result = "Sign in"
actual_result = driver.find_element(By.XPATH, '//h1[@class="a-spacing-small"]').text

assert expected_result in actual_result, f"Error: expected_result ({expected_result}) not present in actual_result ({actual_result})"

print("2. 'Sign in' h1 tag is present on the page")

# Assert that the 'Email or mobile phone number' label is present.
expected_result = "Email or mobile phone number"
actual_result = driver.find_element(By.XPATH, '//label[@for="ap_email"]').text

assert expected_result in actual_result, f"Error: expected_result ({expected_result}) not present in actual_result ({actual_result})"

print("3. 'Email or mobile phone number' label tag is present on the page")

driver.quit()
