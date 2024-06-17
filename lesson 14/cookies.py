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

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get('https://www.freeconferencecall.com/global')
# print(driver.get_cookie("country_code"))
# print(driver.get_cookies())

driver.add_cookie({
    "name" : "custom",
    "value" : "1234"
})

before = driver.get_cookie("split")
print(before)

driver.delete_cookie("split")

driver.add_cookie({
    "name" : "split",
    "value" : "111"
})

after = driver.get_cookie("split")
print(after)

pickle.dump(driver.get_cookies(), open(os.getcwd()+"/cookies/cookies.pkl", "wb")) #скачать куки в файл
cookies = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(5)

driver.refresh()

time.sleep(5)