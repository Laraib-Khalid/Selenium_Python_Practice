from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)  # seconds
driver.get("https://opensource-demo.orangehrmlive.com")
wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Pass")
else:
    print("Login Test Fail")

sleep(2)

driver.switch_to.new_window('tab')
# driver = webdriver.Firefox()

driver.get("https://demo.nopcommerce.com/")
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH,"//img[contains(@alt,'nopCommerce demo store')]")))
sleep(2)

driver.close()
