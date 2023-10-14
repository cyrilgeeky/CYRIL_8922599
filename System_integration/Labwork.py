# Importing required libraries

# pip install selenium


from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Setting up the webdriveru88
driver = webdriver.Chrome()

# Navigate to Google homepage
driver.get("https://www.google.com")


#Find the searchbox and pass the text " conestoga college"

search_box = driver.find_element("name", "q")
search_box.send_keys('conestoga college')
search_box.submit()

# Wait for the search results to load
time.sleep(3)  # You can adjust the wait time based on your internet speed

driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3').click()
time.sleep(4)

driver.find_element(By.XPATH, '//*[@id="maincontent"]/div[2]/div/div/div[1]/div/a[3]/span').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="mm-0"]/div[2]/div[1]/div/div[2]/div[2]/div/div[3]/a/span').click()
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="maincontent"]/p[4]/span/span/span/a').click()
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="sidemenu"]/ul/li[1]/a').click()
time.sleep(5)
# Closing the webdriver
driver.close()
