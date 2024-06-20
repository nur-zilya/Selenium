import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "eager"

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://hyperskill.org/login")
main_tab = driver.current_window_handle

FOR_BUSINESS_BUTTON = ("xpath", "//a[text()=' For Business ']")
driver.find_element(*FOR_BUSINESS_BUTTON).click()
list_of_tabs = driver.window_handles
driver.switch_to.window(list_of_tabs[1])
current_tab = driver.current_window_handle

assert current_tab != main_tab
driver.quit() # Закрытие сессии, т.е всего браузера
driver.close() # Закрытие активного окна / вкладки
