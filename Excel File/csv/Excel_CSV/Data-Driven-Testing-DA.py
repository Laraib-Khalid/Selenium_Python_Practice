from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv


csv_file = "Test_Data.csv"
test_data = []

with open(csv_file, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        test_data.append(row)

print(test_data)

# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

for test in test_data:
    time.sleep(5)
    # driver.find_element(By.NAME, "username").send_keys(test["username"])
    # driver.find_element(By.NAME, "password").send_keys(test["password"])
    # driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Enter username
    username_field = driver.find_element(By.NAME, "username")
    username_field.clear()
    username_field.send_keys(test['Username'])

    # Enter password
    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys(test['Password'])

    # Click the login button
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(2)

driver.quit()