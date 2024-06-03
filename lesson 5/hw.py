import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.wikipedia.org/')
logo = driver.find_element("class name", "central-textlogo-wrapper")
search = driver.find_element("id", "searchInput")
search_button = driver.find_element("class name", "search-input")

logo.click()
time.sleep(2)
search.click()
time.sleep(2)
search_button.click()
time.sleep(2)