import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.freeconferencecall.com/global/pl')


email_field = driver.find_element("xpath", "//input[@type='email']")
email_field.send_keys("nuretdinovazi@gmail.com")
print(email_field.get_attribute("value"))
email_field_val = email_field.get_attribute("value")
assert "nuretdinovazi@gmail.com" == email_field_val
time.sleep(3)
email_field.clear()
time.sleep(3)