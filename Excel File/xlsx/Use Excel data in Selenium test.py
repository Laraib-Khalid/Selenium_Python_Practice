from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from ExcelUtils import ExcelUtils

# Path to your Excel
excel_path = "Excel/Test_Data.xlsx"
sheet_name = "Login_Data"

# Load Excel utility
excel = ExcelUtils(excel_path, sheet_name)

# Set Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--lang=en-US")  # Force Chrome language to English (United States)

# Launch Chrome
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Read total rows
rows = excel.get_row_count()

# Loop through Excel data
for r in range(2, rows + 1):  # starting from row 2 (row 1 = header)
    username = excel.read_data(r, 1)
    password = excel.read_data(r, 2)
    expected = excel.read_data(r, 3)
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
    excel.write_data(1, 4, "Test_Status")
    excel.write_data(r, 4, result)

driver.quit()
