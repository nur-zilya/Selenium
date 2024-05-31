import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.wikipedia.org/')
#
# url = driver.current_url
#
# current_title = driver.title
# print(current_title)
#
# assert url == "https://www.wikipedia.org/", "Url is not correct"

print(driver.page_source)