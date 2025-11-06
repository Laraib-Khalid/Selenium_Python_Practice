from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from CSV_Excel_Utils import CSV_Excel_Utils

# Path to your CSV file
csv_path = "Excel_CSV/Test_Data.csv"

# Load CSV utility
csv_util = CSV_Excel_Utils(csv_path)

# Set Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--lang=en-US")  # Force Chrome language to English (United States)

# Launch Chrome
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Read total rows
rows = csv_util.get_max_rows()

# ✅ Write header for test result column only once
csv_util.write_cell(1, 4, "Test_Status")


# Loop through Excel data
for r in range(2, rows + 1):  # starting from row 2 (row 1 = header)
    username = csv_util.read_cell(r, 1)
    password = csv_util.read_cell(r, 2)
    expected = csv_util.read_cell(r, 3)
    time.sleep(5)
    # Perform login using data from Excel
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(2)
    # Example: check page title or some success message
    if "dashboard" in driver.current_url.lower():
        result = "Success"
    else:
        result = "Failure"

    # Write result back to Excel
    csv_util.write_cell(r, 4, result)

driver.quit()
