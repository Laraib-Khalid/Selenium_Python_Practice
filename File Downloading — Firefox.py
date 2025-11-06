import os
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


# Create download directory if not exists
download_path = os.path.join(os.getcwd(), "Download", "Firefox_Files")
os.makedirs(download_path, exist_ok=True)

# Firefox options setup
options = webdriver.FirefoxOptions()
options.set_preference("browser.download.dir", download_path)
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")

driver = webdriver.Firefox(options=options)
driver.maximize_window()
driver.get("https://omayo.blogspot.com/p/page7.html")
driver.find_element(By.LINK_TEXT,"ZIP file").click()
time.sleep(5)
# --------------------------------------------------------
# STEP 6: Verify if the ZIP file is downloaded successfully
# --------------------------------------------------------
# Check all files in the download directory
downloaded_files = os.listdir(download_path)
print(f"Files in download folder: {downloaded_files}")

# Find any file ending with .zip
zip_files = [f for f in downloaded_files if f.endswith(".zip")]

if zip_files:
    print(f"✅ Download successful! ZIP file found: {zip_files[0]}")
else:
    print("❌ Download failed! No ZIP file found in the download directory.")
driver.quit()