from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
wait = WebDriverWait(driver,10)

# Create ActionChains object
actions = ActionChains(driver)

# Scroll dropdown
dropdown = driver.find_element(By.XPATH,"//input[@id='comboBox']")
dropdown.click()
wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='dropdown']")))
dropdown_option = driver.find_element(By.XPATH,"//div[text()='Item 65']")
actions.move_to_element(dropdown_option).perform()
time.sleep(10)
dropdown_option.click()


time.sleep(10)
