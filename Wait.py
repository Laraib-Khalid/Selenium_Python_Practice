from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Implicit wait (applies to all elements)
driver.implicitly_wait(10)

# Open first site
driver.get("https://opensource-demo.orangehrmlive.com/")

# WebDriver commands
print("Title:", driver.title)
print("URL:", driver.current_url)
print("Page source length:", len(driver.page_source))

# Login
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

# Explicit wait for Dashboard
wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")))

# Conditional methods
dashboard_header = driver.find_element(By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")
print("Is Dashboard displayed?", dashboard_header.is_displayed())
print("Dashboard label text (language-dependent):", dashboard_header.text)

# Navigate to 'My Info'
driver.find_element(By.XPATH, "//span[text()='My Info']").click()
time.sleep(2)

# Checkbox Handling
# Navigate to 'Emergency Contacts' (has checkboxes for delete)
driver.find_element(By.LINK_TEXT, "Emergency Contacts").click()
time.sleep(2)


# Using find_elements (will return list of elements)
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print("Number of checkboxes found:", len(checkboxes))


if len(checkboxes) > 1:
    checkbox = checkboxes[0]
    # Check if the checkbox is enabled and not already selected
    if checkbox.is_enabled() and not checkbox.is_selected():
        driver.execute_script("arguments[0].click();", checkbox)
        print("Second checkbox selected using JavaScript.")



# Text vs get_attribute()
element = driver.find_element(By.XPATH, "//h6[text()='Assigned Emergency Contacts']")
print("Text:", element.text)
print("Tag name using get_attribute:", element.get_attribute("outerHTML"))
time.sleep(10)

# Navigational commands
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(5)
# close() vs quit()
# driver.close()  # Closes current tab only
driver.quit()      # Closes all tabs and ends session

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# # Set up driver with browser language (optional - for testing)
# options = webdriver.ChromeOptions()
# options.add_argument("--lang=en")  # Change to 'fr', 'es', etc. if needed
# driver = webdriver.Chrome(options=options)
#
# driver.maximize_window()
#
# # Implicit wait
# driver.implicitly_wait(10)
#
# # Open site
# driver.get("https://opensource-demo.orangehrmlive.com/")
#
# # WebDriver commands
# print("Title:", driver.title)
# print("URL:", driver.current_url)
# print("Page source length:", len(driver.page_source))
#
# # Login
# driver.find_element(By.NAME, "username").send_keys("Admin")
# driver.find_element(By.NAME, "password").send_keys("admin123")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()
#
# # Wait for Dashboard (don't rely on visible text)
# wait = WebDriverWait(driver, 10)
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.oxd-topbar-header-title > h6")))
#
# # Conditional methods
# dashboard_header = driver.find_element(By.CSS_SELECTOR, "div.oxd-topbar-header-title > h6")
# print("Is Dashboard displayed?", dashboard_header.is_displayed())
# print("Dashboard label text (language-dependent):", dashboard_header.text)
#
# # Navigate to 'My Info' (text may vary)
# driver.find_element(By.XPATH, "//span[contains(@class, 'oxd-main-menu-item') and contains(text(), '')]").click()
# # Or use index-based selection:
# # driver.find_elements(By.CSS_SELECTOR, ".oxd-main-menu-item")[6].click()  # 7th item usually 'My Info'
# time.sleep(2)
#
# # Go to 'Emergency Contacts' tab (partial match for any language)
# driver.find_element(By.XPATH, "//a[contains(@href, 'emergencyContact')]").click()
# time.sleep(2)
#
# # Handle checkboxes
# checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
# print("Number of checkboxes found:", len(checkboxes))
#
# if len(checkboxes) > 1:
#     checkbox = checkboxes[0]
#     if checkbox.is_enabled() and not checkbox.is_selected():
#         driver.execute_script("arguments[0].click();", checkbox)
#         print("Checkbox selected using JavaScript.")
#
# # Text vs get_attribute (language-dependent label)
# element = driver.find_element(By.CSS_SELECTOR, "div.orangehrm-card-container h6")
# print("Text:", element.text)
# print("HTML Tag:", element.get_attribute("outerHTML"))
#
# # Wait before closing
# time.sleep(10)
# driver.quit()
