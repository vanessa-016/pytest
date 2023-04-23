#### Welcome new app ############

import requests 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome('Documents/chromedriver.exe')
url = "https://www.jetbrains.com/es-es/pycharm/"
driver.get(url)
time.sleep(10)