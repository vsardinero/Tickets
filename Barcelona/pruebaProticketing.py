import time
import winsound
import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller
import sectores

keyboard = Controller()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", options=chrome_options)

url = 'https://proticketing.com/realmadrid_futbol/es_ES/entradas/evento/26217/session/1498360/select?viewCode=V_EstadioSantiagoBernabu'

driver.get(url)
wait = WebDriverWait(driver, 120)
wait50 = WebDriverWait(driver, 50)

cookie = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/button[1]/span")))
time.sleep(1)


try:
    cookie.click()
except selenium.common.exceptions.ElementClickInterceptedException:
    print('***Ha saltado la excepcion de las cookies***')
    webdriver.ActionChains(driver).move_to_element(cookie).click(cookie).perform()

currentUrl = url

print(currentUrl)

urlparteuno = currentUrl[0:79]
urlpartedos = int(currentUrl[79:86])
urlpartetres = currentUrl[86:]

print(urlparteuno)
print(urlpartedos)
print(urlpartetres)

counter = urlpartedos
print('contador es: ' + str(counter))

while 1 < 2:
    time.sleep(1)
    driver.get(urlparteuno + str(counter) + urlpartetres)

    try:
        URLencontrada = driver.find_element_by_id('memberUser')

        if URLencontrada == True:
            counter = counter + 1
            print('pagina encontrada!!!!!!!!!!!!!!!!')
            time.sleep(1000)

    except selenium.common.exceptions.NoSuchElementException:
        counter = counter + 1



