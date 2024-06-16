import time
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
wait = WebDriverWait(driver, 5, poll_frequency=1) #передаем ожидание и частоту запросов на выполнения условяи

# driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

#make screenshot
# driver.save_screenshot("screen.png")

driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
time.sleep(5)