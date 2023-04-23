import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome('Documents/chromedriver.exe')

url='https://duckduckgo.com/?t=hc&va=b'
driver.get(url)

driver.find_element(By.NAME,'q').send_keys('Toledo')
driver.find_element(By.ID,'search_button_homepage').click()
driver.find_element(By.XPATH,'//*[@id="r1-0"]/div[1]/div/a').click()

driver.close()

