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
driver.find_element(By.CSS_SELECTOR, '#nav-link-accountList-nav-line-1').click()
# Click 'Create your Amazon account' button to reach 'Registration' page.
driver.find_element(By.CSS_SELECTOR, '#createAccountSubmit').click()

# Amazon logo
driver.find_element(By.CSS_SELECTOR, 'i[aria-label="Amazon"]')
# Create Account Title
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
# Your name input field
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name[placeholder='First and last name']")
# Email input field
driver.find_element(By.CSS_SELECTOR, "input#ap_email[type='email']")
# Password input field
driver.find_element(By.CSS_SELECTOR, "input#ap_password[type='password']")
# Password alert info text
driver.find_element(By.CSS_SELECTOR, ".auth-require-fields-match-group .auth-inlined-information-message[aria-live='polite']")
# Reenter password input field
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check[name='passwordCheck']")
# Continue button
driver.find_element(By.CSS_SELECTOR, "input#continue[type='submit']")
OR
driver.find_element(By.CSS_SELECTOR, "input#continue[aria-labelledby='auth-continue-announce']")
# 'Conditions of Use' hyperlink
driver.find_element(By.CSS_SELECTOR, "a[href*='condition_of_use']")
# 'Privacy Notice' hyperlink
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")
# 'Sign In' hyperlink
driver.find_element(By.CSS_SELECTOR, "a[href*='ap/signin']")

driver.quit()
