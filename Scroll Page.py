from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains, Keys
import time

# Launch Chrome browser and open the URL
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

# Create a WebDriverWait object
wait = WebDriverWait(driver, 10)

# Create ActionChains object for performing advanced user interactions
actions = ActionChains(driver)

# Pause for page to load completely
time.sleep(5)

# Locate the footer link element
Page = driver.find_element(By.XPATH, "//*[@id='Attribution1']/div[1]/a[1]")

# Scroll to the element using ActionChains
actions.move_to_element(Page).perform()

# Scroll to the element using JavaScript (alternative method)
driver.execute_script("arguments[0].scrollIntoView();", Page)

# Pause to observe the scroll
time.sleep(5)

# Scroll to top of the page
driver.execute_script("window.scrollTo(0, 0)")

# Pause to observe scroll
time.sleep(5)

# Scroll to bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# Pause to observe scroll
time.sleep(5)

# Try scrolling up using keyboard key (PAGE_UP) on element (may not work if not focusable)
Page.send_keys(Keys.PAGE_UP)

time.sleep(5)

# Try scrolling down using keyboard key (PAGE_DOWN) on element
Page.send_keys(Keys.PAGE_DOWN)

time.sleep(5)

# Take screenshot in base64 format for embedding into HTML
timestamp = time.strftime("%Y%m%d-%H%M%S")
screenshot_base64 = driver.get_screenshot_as_base64()

# Print base64 string to console (can be embedded in reports)
print(screenshot_base64)

# Generate HTML content with embedded screenshot
html_content = f"""
<html>
  <head><title>Test Screenshot {timestamp}</title></head>
  <body>
    <h2>Screenshot Taken at {timestamp}</h2>
    <img src="data:image/png;base64,{screenshot_base64}" alt="Screenshot" style="max-width:100%; border:2px solid #444;"/>
  </body>
</html>
"""

# Save HTML report to file
with open("report.html", "w") as file:
    file.write(html_content)

# Keep browser open for 10 seconds to view final state before quitting
time.sleep(10)
