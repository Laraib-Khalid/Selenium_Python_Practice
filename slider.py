from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

actions = ActionChains(driver)

# Locate both slider handles
handles = driver.find_elements(By.CLASS_NAME, "ui-slider-handle")
min_handle = handles[0]
max_handle = handles[1]

# Move min handle to the right (e.g., 40px)
actions.click_and_hold(min_handle).move_by_offset(-20, 0).release().perform()
sleep(5)

# Move max handle to the left (e.g., -60px)
actions.click_and_hold(max_handle).move_by_offset(60, 0).release().perform()
sleep(20)
