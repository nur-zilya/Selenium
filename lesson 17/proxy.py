import time
from selenium import webdriver

PROXY = "216.87.69.230:8383"  # Указываем адрес прокси-сервера

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--proxy-server={PROXY}")  # Добавляем прокси через опции
chrome_options.page_load_strategy = "eager"


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://2ip.ru")  # Проверяем IP-адрес

time.sleep(5)