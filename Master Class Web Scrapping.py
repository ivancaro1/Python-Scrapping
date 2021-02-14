import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

chrome_driver = webdriver.Chrome("chromedriver.exe")
chrome_driver.get("https://login.one.com/mail")

correo = chrome_driver.find_element_by_name("displayUsername")
correo.send_keys("alvaro.chiruou@gmail.com")

correo = chrome_driver.find_element_by_name("password")
correo.send_keys("cualquiera")

time.sleep(2)

correo.send_keys(Keys.ENTER)

time.sleep(2)

driver = chrome_driver

driver.execute_script("window.open('');")

time.sleep(2)

driver.switch_to.window(driver.window_handles[1])
driver.get("https://educa.mastech.academy")

driver.close()