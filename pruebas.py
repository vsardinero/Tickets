import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin


gl = GoLogin({
 'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MTM0YTQ0NmEwNzYzMDU2ZjkxM2Y1MTEiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MTM0ZTI2OTllMjRmZTI4ZTBiOTc1N2QifQ.7bTkxXSzMOoOwKXny3lGjBXZqsbtEh2s-XDgsw6zjUo',
 'profile_id': 'yU0Pr0f1leiD',
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
driver.get("http://www.python.org")
assert "Python" in driver.title
driver.close()
time.sleep(3)
gl.stop()