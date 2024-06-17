import os
import time
import pickle
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait #для того, чтобы мы могли указать общее время ожидания для всех условий в будущем.
from selenium.webdriver.support import expected_conditions as EC #ыбрать необходимое условие выполнения которого мы будем ожидать

options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
options.page_load_strategy = 'eager'

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("https://demoqa.com/selectable")
GRID = driver.find_element("xpath", "//*[@id='demo-tab-grid']")
GRID.click()

ONE = ("xpath", "//*[@id='row1']/li[1]")
driver.find_element(*ONE).click()
assert "active" in driver.find_element(*ONE).get_attribute("class"), "Кнпока 'один' не выбрана"

THREE = driver.find_element("xpath", "//*[@id='row1']/li[3]")
THREE.click()
assert "active" in THREE.get_attribute("class"), "Кнпока 'три' не выбрана"

driver.find_element(*ONE).click()
THREE.click()

assert "active" not in driver.find_element(*ONE).get_attribute("class"), "Кнпока 'один' все еще выбрана"
assert "active" not in THREE.get_attribute("class"), "Кнпока 'три' все еще выбрана"
