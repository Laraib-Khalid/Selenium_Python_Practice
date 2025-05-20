import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH,"//img[contains(@alt,'nopCommerce demo store')]")))
time.sleep(2)
driver.close()