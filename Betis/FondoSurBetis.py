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

driver.get("https://proticketing.com/realmadrid_futbol/es_ES/entradas/evento/26217/session/1494237/select?viewCode=V_FondoSur")
wait = WebDriverWait(driver, 120)
wait50 = WebDriverWait(driver, 50)

cookie = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/button[1]/span")))

try:
    cookie.click()
except selenium.common.exceptions.ElementClickInterceptedException:
    print('***Ha saltado la excepcion de las cookies***')
    webdriver.ActionChains(driver).move_to_element(cookie).click(cookie).perform()


def loginSocio():

    socio = '63949'
    password = '120697'

    socio2 = '649542'


    driver.find_element_by_id('memberUser').send_keys(socio)
    driver.find_element_by_id('memberPwd').send_keys(password)
    driver.find_element_by_id('sale-member-submit').click()

    time.sleep(1)

    '''driver.find_element_by_id('memberUser').send_keys(socio2)
    driver.find_element_by_id('memberPwd').send_keys(password)
    driver.find_element_by_id('sale-member-submit').click()'''

def mapaGeneral():
    contador = 0

    while contador != 40:
        try:
            cargaSectores = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="DEDB0221-D0AA-DD29-89CA-2E7EE60DC05A"]')))
            keyboard.tap(Key.end)

            dispoNo = driver.find_elements_by_xpath('//*[@class="interactive disabled"]')
            dispoSi = driver.find_elements_by_xpath('//*[@class="interactive"]')
            print('Dispo NO - ' + str(len(dispoNo)))
            print('Dispo SI - ' + str(len(dispoSi)))

            if len(dispoSi) != 0:
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                try:
                    dispoSi[0].click()

                except selenium.common.exceptions.JavascriptException:
                    driver.execute_script("arguments[0].click();", dispoSi[0])

                except selenium.common.exceptions.ElementClickInterceptedException:
                    webdriver.ActionChains(driver).move_to_element(dispoSi[0]).click(dispoSi[0]).perform()


                time.sleep(700)

            else:
                driver.refresh()
                contador += 1
                print('Refresh numero ' + str(contador))

                if contador == 40:
                    print('***Vuelta a empezar***')
                    contador = 0
                    time.sleep(60)

        except TimeoutException:
            driver.get("https://proticketing.com/realmadrid_futbol/es_ES/entradas/evento/26217/session/1494237/select?viewCode=V_FondoSur")

def mapaSectores():

    lugar = ('FondoSur')
    driver.get("https://proticketing.com/realmadrid_futbol/es_ES/entradas/evento/26217/session/1494237/select?viewCode=V_"+ lugar)

    contador = 0

    while contador != 40:
        try:
            cargaSectores = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="interactive disabled"]')))
            keyboard.tap(Key.end)

            dispoNo = driver.find_elements_by_xpath('//*[@class="interactive disabled"]')
            dispoSi = driver.find_elements_by_xpath('//*[@class="interactive"]')
            print('Dispo Sectores NO - ' + str(len(dispoNo)))
            print('Dispo Sectores SI - ' + str(len(dispoSi)))

            if len(dispoSi) != 0:
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                try:
                    dispoSi[0].click()

                except selenium.common.exceptions.JavascriptException:
                    driver.execute_script("arguments[0].click();", dispoSi[0])

                except selenium.common.exceptions.ElementClickInterceptedException:
                    webdriver.ActionChains(driver).move_to_element(dispoSi[0]).click(dispoSi[0]).perform()

                cargaAsientos = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="button secondary expand back ng-binding"]')))
                print("**carga asientos OK**")

                asientosLibres = driver.find_elements_by_xpath('//*[@class="interactive available-seat"]')
                asientosOcupados = driver.find_elements_by_xpath('//*[@class="unavailable-seat"]')
                print('Asientos ocupados - ' + str(len(asientosOcupados)))
                print('Asientos libres - ' + str(len(asientosLibres)))

                if len(asientosLibres) > 1:
                    for i in asientosLibres:
                        i.click()

                    print('Empieza el letargo')
                    time.sleep(700)

                else:
                    driver.back()

                #seleccionAsientos()


            else:
                driver.refresh()
                contador += 1
                print('Refresh numero ' + str(contador))

                if contador == 40:
                    print('***Vuelta a empezar***')
                    contador = 0
                    time.sleep(60)


        except TimeoutException:
            driver.get("https://proticketing.com/realmadrid_futbol/es_ES/entradas/evento/26217/session/1494237/select?viewCode=V_" + lugar)

def seleccionAsientos():
    cargaAsientos = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="unavailable-seat disabled"]')))
    keyboard.tap(Key.end)

    asientosLibres = driver.find_elements_by_xpath('//*[@class="interactive available-seat"]')
    asientosOcupados = driver.find_elements_by_xpath('//*[@class="unavailable-seat disabled"]')
    print('Asientos ocupados - ' + str(len(asientosOcupados)))
    print('Asientos libres - ' + str(len(asientosLibres)))

    try:
        asientosLibres[0].click()

    except selenium.common.exceptions.JavascriptException:
        driver.execute_script("arguments[0].click();", asientosLibres)

    if asientosLibres[1] or asientosLibres[2] or asientosLibres[3] or asientosLibres[4] or asientosLibres[5]:
        time.sleep(0.2)
        asientosLibres[1].click()
        asientosLibres[2].click()
        asientosLibres[3].click()
        asientosLibres[4].click()
        asientosLibres[5].click()

    contadorAsientos = 0


    if len(asientosLibres) == 0:
        while contadorAsientos != 40:

            driver.refresh()
            contadorAsientos += 1
            print('Refresh Asientos libres - ' + str(contadorAsientos))

    print('Sleep de seleccion de asientos')
    time.sleep(700)

def sectorObjetivo():
    contador = 0
    driver.get('https://proticketing.com/realmadrid_futbol/es_ES/entradas/evento/22282/session/1274936/select?_ga=2.97099615.1973057075.1650877872-1206011927.1647002764&viewCode=V_438')

    while contador != 40:
        try:
            cargaAsientos = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="unavailable-seat disabled"]')))
            keyboard.tap(Key.end)
            asientosLibres = driver.find_elements_by_xpath('//*[@class="interactive available-seat"]')
            asientosOcupados = driver.find_elements_by_xpath('//*[@class="unavailable-seat disabled"]')
            print('Asientos ocupados - ' + str(len(asientosOcupados)))
            print('Asientos libres - ' + str(len(asientosLibres)))

            if len(asientosLibres) != 0:

                try:
                    asientosLibres[0].click()

                except selenium.common.exceptions.JavascriptException:
                    driver.execute_script("arguments[0].click();", asientosLibres)

                if asientosLibres[1] or asientosLibres[2] or asientosLibres[3]:
                    time.sleep(0.2)
                    asientosLibres[1].click()
                    asientosLibres[2].click()
                    asientosLibres[3].click()

            else:
                driver.refresh()
                contador += 1

                if contador == 40:
                    cuenta = 0
                    print('***A esperar***')

        except TimeoutException:
            driver.get("https://proticketing.com/realmadrid_futbol/es_ES/entradas/evento/22282/session/1274936/select?_ga=2.97099615.1973057075.1650877872-1206011927.1647002764&viewCode=V_FondoSur")

mapaSectores()




