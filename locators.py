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

# search by ID
driver.find_element(By.ID, 'nav-search-submit-button')
driver.find_element(By.ID, 'twotabsearchtextbox')

# search textfield by XPATH
driver.find_element(By.XPATH, '//input[@aria-label="Search Amazon"]')
driver.find_element(By.XPATH, '//input[@name="field-keywords"]')

# search button by ID
driver.find_element(By.XPATH, '//input[@id="nav-search-submit-button"]')
driver.find_element(By.XPATH, '//input[@class="nav-input nav-progressive-attribute" and @value="Go"]')

# search h2 by text()
driver.find_element(By.XPATH, '//h2[text()="New from Victoria\'s Secret"]')

# search anchor tag by text() + and
driver.find_element(By.XPATH, '//a[text()="Best Sellers" and @class="nav-a  "]')

# search anchor tag by contains()
driver.find_element(By.XPATH, '//h2[contains(text(), "Scary-good")]')

# search by combining
driver.find_element(By.XPATH, '//div[@id="nav-main"]//a[text()="Best Sellers"]')

driver.quit()
