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

# wait for 4 sec
sleep(4)

# Click 'Sign In' icon in Top Navigation.
driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Account, sign in"]').click()

# wait for 4 sec
sleep(4)

# Click 'Sign In' in the sidebar.
button = driver.find_element(By.CSS_SELECTOR, 'a[data-test="accountNav-signIn"]')
sleep(4)
driver.execute_script("arguments[0].click();", button)

sleep(4)
# Assert that the 'www.target.com/login' is present in the url.
expected_in_url = "www.target.com/login"
current_url = driver.current_url.lower()
assert expected_in_url in current_url, f"1. Error: '{expected_in_url}' is not present in Current URL ({current_url})"
print(f"1. '{expected_in_url}' is present in the Current URL")

# wait for 4 sec
sleep(4)

# Assert that the 'Sign into your Target account' message appears in the sidebar form.
expected_message = "Sign into your Target account"
actual_message = driver.find_element(By.XPATH, '//span[contains(text(), "Sign into your Target account")]').text
assert expected_message in actual_message, f"2. Error: expected_result ({expected_message}) not present in actual_result ({actual_message})"
print(f"2. '{expected_message}' message is present on the page")

# Assert that the 'Sign in' button appears in the sidebar form.
sign_in_button = driver.find_element(By.CSS_SELECTOR, "button#login[type='submit']")
assert sign_in_button is not None, f"3. 'Sign In' button not present"
print(f"3. 'Sign In' button is present in the sidebar form")

driver.quit()
