import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://vk.ru')

time.sleep(3)

driver.back() #возвращает на предыд. страницу

time.sleep(3)

driver.forward() #переходит на след. стр

time.sleep(3)

driver.refresh() #обновляет страницу

time.sleep(3)