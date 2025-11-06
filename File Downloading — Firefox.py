import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


# Create download directory if not exists
download_path = os.path.join(os.getcwd(), "Download", "Firefox_Files")
os.makedirs(download_path, exist_ok=True)

# Firefox options setup
options = webdriver.FirefoxOptions()
options.set_preference("browser.download.dir", download_path)
options.set_preference("browser.download.folderList", 2)
# options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")
options.set_preference(
    "browser.helperApps.neverAsk.saveToDisk",
    "application/zip,application/pdf,image/jpeg,image/png,image/gif,image/tiff,image/x-icon,image/svg+xml,image/webp"
)


driver = webdriver.Firefox(options=options)
driver.maximize_window()
# driver.get("https://omayo.blogspot.com/p/page7.html")
# # driver.find_element(By.LINK_TEXT,"ZIP file").click()
# time.sleep(5)
#
#
# driver.switch_to.new_window('tab')
driver.get("https://practice.expandtesting.com/download")
# # Pause execution here until user presses Enter
# input("🚀 Execution paused. Press Enter to resume...")

page = driver.find_element(By.XPATH,"//a[@href='download/cdct.jpg']")
# Scroll to the element using ActionChains
# actions = ActionChains(driver)
# actions.move_to_element(page).perform()

page.click()
time.sleep(5)


# --------------------------------------------------------
# STEP 6: Verify if the ZIP file is downloaded successfully
# --------------------------------------------------------
# Check all files in the download directory
downloaded_files = os.listdir(download_path)
print(f"Files in download folder: {downloaded_files}")

ext = [".zip", ".pdf", ".jpg"]
# Find any file ending with .zip
for ext in ext:
    zip_files = [f for f in downloaded_files if f.endswith(ext)]

    if zip_files:
        print(f"✅ {ext.strip(".")} file found: {zip_files[0]}")
        break
    else:
        print(f"❌ No {ext.strip(".")} file found in the download directory.")
driver.quit()