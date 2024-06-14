import time
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
preferences = {
    "download.default_directory" : os.path.join(os.getcwd(), f"{os.getcwd()}/downloads") # Универсальный путь для всех систем
}
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
chrome_options.add_experimental_option("prefs", preferences)

driver.get('http://the-internet.herokuapp.com/download')

elements = driver.find_elements('xpath', " //*[@id = 'content']/div/a[@href]")
for el in elements:
    el.click()
