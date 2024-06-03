import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://hyperskill.org/tracks')

buttons = driver.find_elements(By.XPATH, "//button[contains(@class, 'btn')]")

print(len(buttons))

time.sleep(5)
driver.quit()

# //div[@class=’table’] - по классу
# //employee[@id=’2’] - по id
# //employee[@id=’1’]/name[text()=’David’] - по тексту
# //name[text()=’John’] - по тексту