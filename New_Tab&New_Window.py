from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Open main window
driver.get("https://example.com")

# Open a new tab
driver.switch_to.new_window('tab')
driver.get("https://google.com")
time.sleep(5)

# Open a new window
driver.switch_to.new_window('window')
driver.get("https://bing.com")

time.sleep(5)

# Open a new tab using JavaScript
driver.execute_script("window.open('https://youtube.com', '_blank');")
time.sleep(5)


driver.quit()
