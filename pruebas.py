import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin


gl = GoLogin({
 'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MzE0YTI2YzUzNjc5YjczZGFlN2ZlNjMiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MzE1YTQyNzE5YmM0OTQ5MmZmZjM3M2YifQ.S-FPJC1i3ho1mqBl5MNFKGSd4iRG7mKs5oNBL6mpTR4',
 'profile_id': '6314a318fd572452d1040ebd',
})

if platform == "linux" or platform == "linux2":
 chrome_driver_path = './chromedriver'
elif platform == "darwin":
 chrome_driver_path = './mac/chromedriver'
elif platform == "win32":
 chrome_driver_path = 'C:\\chromedriver.exe'

debugger_address = gl.start()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", debugger_address)
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", options=chrome_options)
driver.get("url://www.python.org")
assert "Python" in driver.title
driver.close()
time.sleep(3)
gl.stop()