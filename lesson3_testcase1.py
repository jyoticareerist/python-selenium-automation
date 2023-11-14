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
driver.get('https://www.target.com/')

# Click 'Carts' icon.
driver.find_element(By.CSS_SELECTOR, 'a[href*=cart]').click()

# Assert that the 'www.target.com/cart' is present in the url.
expected_in_url = "www.target.com/cart"
current_url = driver.current_url.lower()

assert expected_in_url in current_url, f"1. Error: '{expected_in_url}' is not present in Current URL ({current_url})"

print(f"1. '{expected_in_url}' is present in the Current URL")

# wait for 4 sec
sleep(4)

# Assert that the 'Your cart is empty' message is present.
expected_result = "Your cart is empty"
actual_result = driver.find_element(By.XPATH, '//h1[contains(text(), "Your cart is empty")]').text

assert expected_result in actual_result, f"2. Error: expected_result ({expected_result}) not present in actual_result ({actual_result})"

print(f"2. '{expected_result}' message is present on the page")

driver.quit()
