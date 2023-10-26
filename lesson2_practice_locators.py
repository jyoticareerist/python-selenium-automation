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

# Click 'Hello, sign in' in Top Navigation to reach 'Sign In' page.
driver.find_element(By.ID, 'nav-link-accountList-nav-line-1').click()

# Amazon logo
driver.find_element(By.XPATH, '//i[@aria-label="Amazon"]')
# Email field
driver.find_element(By.ID, "ap_email")
driver.find_element(By.NAME, "email")
driver.find_element(By.XPATH, '//input[@type="email" and @class="a-input-text a-span12 auth-autofocus auth-required-field"]')
# Continue button
driver.find_element(By.XPATH, '//input[@aria-labelledby="continue-announce"]')
# OR
driver.find_element(By.XPATH, '//span[@id="continue" and @class="a-button a-button-span12 a-button-primary"]')
# Conditions of use link
driver.find_element(By.XPATH, '//a[text()="Conditions of Use"]')
# Privacy Notice link
driver.find_element(By.XPATH, '//a[text()="Privacy Notice"]')
# Need help link
driver.find_element(By.XPATH, '//span[contains(text(), "Need help")]')
# Forgot your password link
driver.find_element(By.ID, "auth-fpp-link-bottom")
driver.find_element(By.XPATH, '//a[contains(text(), "Forgot your password")]')
# Other issues with Sign-In link
driver.find_element(By.ID, "ap-other-signin-issues-link")
driver.find_element(By.XPATH, '//a[contains(text(), "Other issues with Sign-In")]')
# Create your Amazon account button
driver.find_element(By.ID, "createAccountSubmit")
driver.find_element(By.XPATH, '//a[@id="createAccountSubmit" and @class="a-button-text"]')
# OR
driver.find_element(By.ID, "auth-create-account-link")
driver.find_element(By.XPATH, '//span[@id="auth-create-account-link" and @class="a-button a-button-span12 a-button-base"]')

driver.quit()
