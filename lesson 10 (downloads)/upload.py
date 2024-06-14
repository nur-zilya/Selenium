import time
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://demoqa.com/upload-download')

upload_file_field = driver.find_element('xpath', "//input[@id='uploadFile']")
upload_file_field.send_keys(os.path.join(os.getcwd(), "decomposition.png"))

time.sleep(5)


