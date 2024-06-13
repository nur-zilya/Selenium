import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito") #запускает браузер в режиме без графического интерфейса. Это позволяет выполнять тесты в фоновом режиме без отображения окна браузера.
# chrome_options.add_argument("--headless") #апускает браузер в режиме инкогнито
chrome_options.add_argument("--ignore-certificate-errors")#игнорирует ошибки сертификата SSL
chrome_options.add_argument("--window-size=500,200") #размер окна браузера
chrome_options.add_argument("--disable-cache") #отключает кэширование в браузере
# chrome_options.page_load_strategy = 'normal' #используется по дефолту и ожидает загрузки всех ресурсов (картинки, js-код, шрифты и т.д) на странице
chrome_options.page_load_strategy = 'eager' #ожидает только готовности загрузки DOM (html-структуры), но при этом картинки и прочее может до сих пор грузиться.
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://the-internet.herokuapp.com/status_codes')
time.sleep(3)