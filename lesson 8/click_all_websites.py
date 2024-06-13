import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://the-internet.herokuapp.com/status_codes')
time.sleep(2)
links = driver.find_elements("xpath", "//li/a")
for link in links:
    link.click()
    time.sleep(3)
    driver.back()
    time.sleep(2)
