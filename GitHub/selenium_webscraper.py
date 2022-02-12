#i used chocolately to get geckodriver using the below
#choco install selenium-gecko-driver

#get those libraries in here
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as firefoxOptions
from selenium.webdriver.firefox.service import Service
driver = webdriver.Firefox()
driver.get('https://www.adafruit.com/product/3775') 
driver.implicitly_wait(5)
time.sleep(2)

stock = driver.find_element(By.CLASS_NAME, "oos-header")
price = driver.find_element(By.CLASS_NAME, 'product-price')
name_pi = driver.find_element(By.CLASS_NAME, 'product-name-large')

driver.save_screenshot("C:\\Users\\toutb\\Downloads\\itworked.png")

result_scrape = "This is your daily price watch bot for Adafruit. Today {} is {} and has a price of {}".format(name_pi, stock.text, price)
print(result_scrape)

driver.quit()
