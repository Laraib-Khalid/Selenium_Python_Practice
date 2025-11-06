from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://letcode.in/calendar")

# Method 1: Direct send_keys
# driver.find_element(By.ID, "birthday").send_keys("06-11-2025")

# Click the input box to open date picker
# driver.find_element(By.ID, "birthday").click()

date_input = driver.find_element(By.ID, "birthday")

# Focus the input
date_input.click()
time.sleep(1)

# Press ARROW_DOWN or SPACE to open the calendar icon (browser dependent)
date_input.send_keys(Keys.SPACE)
time.sleep(2)

# Choose a specific date (e.g., 20th of the month)
driver.find_element(By.XPATH, "//div[@class='react-datepicker__day' and text()='20']").click()

time.sleep(5)
driver.quit()
