# from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

# Locate the element to hover over
mouse_hover = driver.find_element(By.XPATH, "//button[@class='dropbtn']")  # Replace with your XPath

# Create ActionChains object
actions = ActionChains(driver)

actions.move_to_element(driver.find_element(By.XPATH,"//h2[@class='title']"))
time.sleep(5)

# Perform mouse hover
hover = actions.move_to_element(mouse_hover)
sub_menu = driver.find_element(By.XPATH,"//a[text()='Mobiles']")
time.sleep(5)
hover.perform()
time.sleep(5)

hover.click(sub_menu).perform()

time.sleep(10)