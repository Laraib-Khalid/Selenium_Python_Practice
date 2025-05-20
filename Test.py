import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
print("Website Title is:", driver.title)
first_tab = driver.window_handles
print("First Tab Id:", first_tab)

time.sleep(5)


driver.find_element(By.XPATH,"//button[text()='New Tab']").click()

# Wait briefly to allow the new tab to open
  # You can replace this with WebDriverWait for more reliability

# Get updated list of tabs
second_tab = driver.window_handles
print("Second Tab Id:", second_tab[1])

# Switch to the second tab (index 1)
driver.switch_to.window(second_tab[1])

# Now get the title of the current page
actual_title = driver.title

# You can then verify it
expected_title = "SDET-QA Blog"
if actual_title == expected_title:
    print("✅ New tab title is correct.")
else:
    print(f"❌ Title mismatch! Expected: '{expected_title}', but got: '{actual_title}'")

time.sleep(10)