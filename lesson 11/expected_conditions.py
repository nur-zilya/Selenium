import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait #для того, чтобы мы могли указать общее время ожидания для всех условий в будущем.
from selenium.webdriver.support import expected_conditions as EC #ыбрать необходимое условие выполнения которого мы будем ожидать

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15, poll_frequency=1) #передаем ожидание и частоту запросов на выполнения условяи

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

ADD_ELEMENT_BUTTON = ("xpath", "//*[@id='content']/div/button")

wait.until(EC.element_to_be_clickable(ADD_ELEMENT_BUTTON), message="Button is not found") # Ждем пока кнопка станет кликабельной
driver.find_element(*ADD_ELEMENT_BUTTON).click()


# element_to_be_clickable(locator) - Ожидает видимости элемента и его кликабельности (возможности кликнуть).
# visibility_of_element_located(locator) - Ожидание проверки того, что элемент присутствует в DOM и виден визуально. Видимость означает, что элемент не только отображается но также имеет высоту и ширину, которые больше 0.
# invisibility_of_element_located(locator) - Ожидание проверки того, является ли элемент невидимым или он исчез из DOM.
# text_to_be_present_in_element(locator, text) - Ожидание наличия нужного текста в элементе.
