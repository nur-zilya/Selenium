import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://demoqa.com/automation-practice-form')

first_name = driver.find_element('xpath', '//input[@id="firstName"]')
first_name.clear()
assert first_name.get_attribute("value") == ""
first_name.send_keys('Alex')
time.sleep(3)

second_name = driver.find_element('xpath', '//input[@id="lastName"]')
second_name.clear()
assert second_name.get_attribute("value") == ""
second_name.send_keys('Petrov')
time.sleep(3)

email = driver.find_element('xpath', '//input[@id="userEmail"]')
email.clear()
assert email.get_attribute("value") == ""
email.send_keys("test@test.com")
time.sleep(3)

phone_number = driver.find_element('xpath', '//input[@id="userNumber"]')
phone_number.clear()
assert phone_number.get_attribute("value") == ""
phone_number.send_keys("+79998765432")
time.sleep(3)

address = driver.find_element('xpath', '//*[@id="currentAddress"]')
address.clear()
assert address.get_attribute("value") == ""
address.send_keys("Spartakovskaya 2, Kazan, Republic of Tatrstan, Russia")
time.sleep(3)