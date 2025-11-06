import os
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# options = webdriver.ChromeOptions()
# if not os.path.exists("Download/Chrome_Files"):
#     # os.mkdir("Download")
#     makedirs("Download/Chrome_Files")
# print(directory_path:=os.getcwd())
# # os.chdir("Download/Chrome_Files")
# prefs = {"download.default_directory":r"directory_path/Download"}

# Create download directory if not exists
download_path = os.path.join(os.getcwd(), "Download", "Chrome_Files")
os.makedirs(download_path, exist_ok=True)

# Chrome options setup
options = webdriver.ChromeOptions()
prefs = {"download.default_directory": download_path}



options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)
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

#
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://omayo.blogspot.com/p/page7.html")