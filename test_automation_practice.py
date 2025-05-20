import time
import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
print("Website Title is:", driver.title)

wait = WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[@class='title']")))
header_text = driver.find_element(By.XPATH,"//h1[@class='title']")
print("Is Dashboard displayed?", header_text.is_displayed())
print("Header Text is:", header_text.text)
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Laraib Khalid")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("laraib.khalid@pk.com")
driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("1234567890")
driver.find_element(By.XPATH,"//textarea[@id='textarea']").send_keys("Automation Testing")

gender_radiobutton = driver.find_elements(By.XPATH,"//input[@name='gender']")
print("Gender radio buttons found:", len(gender_radiobutton))
# gender_radiobutton[0].click()


# Loop and click the one with value='female'
for radio in gender_radiobutton:
    if radio.get_attribute("value").lower() == "female":
        if not radio.is_selected():
            radio.click()
            print("Female gender selected.")
        break

days_checkbox = driver.find_elements(By.XPATH,"//div[@class='form-group']//input[@type='checkbox']")
print("Days checkboxes found:", len(days_checkbox))
# days_checkbox[1].click()

# List of days you want to select
days_to_select = ["monday", "wednesday", "friday"]

# Loop through each checkbox and match by value
for checkbox in days_checkbox:
    value = checkbox.get_attribute("value").lower()
    if value in days_to_select:
        if not checkbox.is_selected():
            checkbox.click()
            print(f"{value.capitalize()} checkbox selected.")

dropdown = driver.find_element(By.XPATH,"//select[@id='country']")
select = Select(dropdown)

# Select by value
select.select_by_value("uk")
print("Country selected:", select.first_selected_option.text)

# Select by visible text
select.select_by_visible_text("Germany")
print("Country selected:", select.first_selected_option.text)

# Select by index
select.select_by_index(6)
print("Country selected:", select.first_selected_option.text)


multi_select_dropdown = driver.find_element(By.XPATH,"//select[@id='colors']")
multi_select = Select(multi_select_dropdown)

if multi_select.is_multiple:
    multi_select.select_by_visible_text("White")
    multi_select.select_by_visible_text("Green")
    multi_select.select_by_visible_text("Blue")
    print("Colors selected:", ", ".join([option.text for option in multi_select.all_selected_options]))

else:
    print("This is not a multi-select dropdown.")

time.sleep(2)

# Deselect green color
multi_select.deselect_by_visible_text("Green")
print("Colors selected that Green color deselected:", ", ".join([option.text for option in multi_select.all_selected_options]))


# # Check if it's a multi-select
# if multi_select.is_multiple:
#     # Loop through all options and select them
#     for option in multi_select.options:
#         multi_select.select_by_visible_text(option.text)
#         print(f"Selected: {option.text}")
# else:
#     print("Dropdown is not multi-select")



# Locate dropdown
dropdown_element = driver.find_element(By.ID, "animals")  # Replace with actual ID
select = Select(dropdown_element)

# Get all option texts
options_text = [option.text for option in select.options]

# Check if options are sorted
if options_text == sorted(options_text):
    print("Dropdown options are sorted.")

    # Select all options if it's a multi-select dropdown
    if select.is_multiple:
        for option in select.options:
            select.select_by_visible_text(option.text)
            print(f"Selected: {option.text}")
    else:
        print("Dropdown is not multi-select. Cannot select all.")
else:
    print("Dropdown options are NOT sorted. Nothing selected.")


driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
driver.find_element(By.XPATH,"//a[@title='Prev']").click()
driver.find_element(By.XPATH,"//a[@data-date='23']").click()


driver.find_element(By.XPATH,"//input[@id='txtDate']").click()
select_month_dropdown = driver.find_element(By.XPATH,"//select[@aria-label='Select month' and @class = 'ui-datepicker-month']")
select_month_dropdown.click()
select_month = Select(select_month_dropdown)
select_month.select_by_visible_text("Mar")

select_year_dropdown = driver.find_element(By.XPATH,"//select[@aria-label='Select year' and @class = 'ui-datepicker-year']")
select_year_dropdown.click()
select_year = Select(select_year_dropdown)
select_year.select_by_visible_text("2018")


driver.find_element(By.XPATH,"//td[@data-handler='selectDay']//a[@data-date='21']").click()


# driver.find_element(By.XPATH,"//input[@id='start-date']").send_keys("12")
# driver.find_element(By.XPATH,"//input[@id='start-date']").send_keys("01")
# driver.find_element(By.XPATH,"//input[@id='start-date']").send_keys("1998")
#
#
# driver.find_element(By.XPATH,"//input[@id='end-date']").send_keys("12")
# driver.find_element(By.XPATH,"//input[@id='end-date']").send_keys("01")
# driver.find_element(By.XPATH,"//input[@id='end-date']").send_keys("2025")
#
# driver.find_element(By.XPATH,"//button[@class='submit-btn']").click()
#
#
# wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='result']")))
#
#  # Locate the div containing result text
# result_div = driver.find_element(By.XPATH,"//div[@class='result']")  # Replace with actual ID or suitable locator
#
# # Get the text from the element
# result_text = result_div.text
#
# # Verify the text contains the expected phrase
# if "You selected a range of" in result_text:
#     print("PASS: Correct range message is displayed.")
# else:
#     print("FAIL: Expected text not found.")


# # Enter start date
# start_date = driver.find_element(By.ID, "start-date")
# start_date.clear()
# start_date.send_keys("12011998")  # MMDDYYYY if that's the format
#
# # Enter end date
# end_date = driver.find_element(By.ID, "end-date")
# end_date.clear()
# end_date.send_keys("12012025")
#
# driver.find_element(By.XPATH,"//button[@class='submit-btn']").click()
#
# # Wait for the result text to appear and contain the expected phrase
# wait = WebDriverWait(driver, 10)
# result = wait.until(EC.visibility_of_element_located((By.ID, "result")))  # Replace ID if different
#
# # Verify the result text
# result_text = result.text
# if "You selected a range of" in result_text:
#     print("PASS: Correct result message displayed.")
#     print("Result Text:", result_text)
# else:
#     print("FAIL: Expected message not found.")


# Define start and end dates
start_date_str = "12/01/1998"
end_date_str = "12/01/2025"

# Enter start date
start_input = driver.find_element(By.ID, "start-date")
start_input.clear()
start_input.send_keys(start_date_str.replace("/", ""))  # e.g., "12011998"

# Enter end date
end_input = driver.find_element(By.ID, "end-date")
end_input.clear()
end_input.send_keys(end_date_str.replace("/", ""))  # e.g., "12012025"

driver.find_element(By.XPATH,"//button[@class='submit-btn']").click()

# Wait for result message
wait = WebDriverWait(driver, 10)
result = wait.until(EC.visibility_of_element_located((By.ID, "result")))  # Replace with actual locator

# Get result text
result_text = result.text
print("Displayed Result:", result_text)

# Verify result contains the expected phrase
if "You selected a range of" in result_text:
    print("PASS: Text contains expected phrase.")

    # Extract number of days from result

    match = re.search(r"(\d+)\s+days", result_text)
    if match:
        displayed_days = int(match.group(1))

        # Calculate actual difference in days
        start_dt = datetime.strptime(start_date_str, "%m/%d/%Y")
        end_dt = datetime.strptime(end_date_str, "%m/%d/%Y")
        actual_days = (end_dt - start_dt).days

        if displayed_days == actual_days:
            print(f"PASS: Displayed days ({displayed_days}) match actual difference ({actual_days}).")
        else:
            print(f"FAIL: Displayed days ({displayed_days}) do NOT match actual ({actual_days}).")
    else:
        print("FAIL: Could not extract number of days from result.")
else:
    print("FAIL: Expected message not found.")

wait.until(EC.visibility_of_element_located((By.XPATH,"//form[@id='singleFileForm']")))

# driver.find_element(By.XPATH,"//input[@id='singleFileInput']").click()
upload_single_input = driver.find_element(By.XPATH,"//input[@id='singleFileInput']")
file_path = r"C:\Users\LaraibKhalid\Downloads\monthly-budget-expenses-spreadsheet-within-business-income-and-expense-spreadsheet-with-template-sheet-to.jpg"
upload_single_input.send_keys(file_path)

driver.find_element(By.XPATH,"//button[text()='Upload Single File']").click()

upload_multiple_input = driver.find_element(By.XPATH,"//input[@id='multipleFilesInput']")

# List of file names (relative or absolute)
file_names = [
    "WhatsApp Image 2025-04-24 at 4.37.27 PM.jpeg",
    "WhatsApp Image 2025-04-24 at 4.37.26 PM (1).jpeg",
    "monthly-budget-expenses-spreadsheet-within-business-income-and-expense-spreadsheet-with-template-sheet-to.jpg"
]

file_paths = [rf"C:\Users\LaraibKhalid\Downloads\{file_name}" for file_name in file_names]
upload_multiple_input.send_keys("\n".join(file_paths))

driver.find_element(By.XPATH,"//button[text()='Upload Multiple Files']").click()




# Locate the table body
rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")

# Loop through each row
for row in rows:
    # Check if the row contains header cells (th)
    header_row = row.find_elements(By.TAG_NAME, "th")
    if header_row:
        header_values = [header.text for header in header_row]
        print("Headers:", header_values)
    else:
        # Find all regular data cells (td) in the row
        cells = row.find_elements(By.TAG_NAME, "td")
        values = [cell.text for cell in cells]
        print("Row:", values)

# Get the specific cell (e.g., 3rd row, 2nd column)
specific_cell = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[3]/td[2]")
print("Specific Cell Value:", specific_cell.text)



# Loop through rows and get the second column values if they exist
second_column_values = [row.find_elements(By.TAG_NAME, "td")[1].text for row in rows if len(row.find_elements(By.TAG_NAME, "td")) > 1]
print("Second Column Values:", second_column_values)


# third_column_rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/td[2]")
# for third_col in third_column_rows:
#     print("Third Column Rows:", third_col.text)


# Locate all 3rd column <td> elements (index 2 means 3rd column)
third_column_elements = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/td[3]")

# Extract text into a list
third_column_values = [elem.text for elem in third_column_elements]

# Print the list
print("Third Column Values:", third_column_values)


# Extract text and get distinct values using set
distinct_third_column_values = list(set([elem.text for elem in third_column_elements]))

# Print the distinct values
print("Distinct Third Column Values:", distinct_third_column_values)




# Locate the table body
dynamic_rows = driver.find_elements(By.XPATH, "//table[@id='taskTable']/tbody/tr")

# Loop through each row
for dynamic_row in dynamic_rows:
        # Find all regular data cells (td) in the row
        dynamic_cells = dynamic_row.find_elements(By.TAG_NAME, "td")
        dynamic_values = [dynamic_cell.text for dynamic_cell in dynamic_cells]
        print("Dynamic Row:", dynamic_values)




driver.find_element(By.XPATH,"//ul[@id='pagination']//li/a[text()='3']").click()

# Locate the table body
productTable_rows = driver.find_elements(By.XPATH, "//table[@id='productTable']//tr")

# Loop through each row
for productTable_row in productTable_rows:
    # Check if the row contains header cells (th)
    productTable_header_row = productTable_row.find_elements(By.TAG_NAME, "th")
    if productTable_header_row:
        productTable_header_values = [productTable_header.text for productTable_header in productTable_header_row]
        print("Headers:", productTable_header_values)
    else:
        # Find all regular data cells (td) in the row
        productTable_cells = productTable_row.find_elements(By.TAG_NAME, "td")
        productTable_values = [productTable_cell.text for productTable_cell in productTable_cells]
        print("Row:", productTable_values)


driver.find_element(By.XPATH,"//table[@id='productTable']//tr[3]//input[@type='checkbox']").click()
driver.find_element(By.XPATH,"//table[@id='productTable']//tr[5]//input[@type='checkbox']").click()



driver.find_element(By.XPATH,"//input[@id='input1']").send_keys("Laraib")
driver.find_element(By.XPATH,"//button[@id='btn1']").click()
driver.find_element(By.XPATH,"//input[@id='input2']").send_keys("Khalid")
driver.find_element(By.XPATH,"//button[@id='btn2']").click()
driver.find_element(By.XPATH,"//input[@id='input3']").send_keys("Masood")
driver.find_element(By.XPATH,"//button[@id='btn3']").click()


driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("Python")
driver.find_element(By.XPATH,"//input[@class='wikipedia-search-button']").click()
wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='wikipedia-search-results']")))
time.sleep(2)
driver.find_element(By.XPATH,"//a[text()='Python (programming language)']").click()
time.sleep(5)

# Get all window handles (tabs)
tabs = driver.window_handles

# Switch to the first tab (index 0)
driver.switch_to.window(tabs[0])


driver.switch_to.new_window('window')
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
time.sleep(2)

windows = driver.window_handles
driver.switch_to.window(windows[0])

dynamic_button = driver.find_element(By.XPATH,"//button[@onclick='toggleButton(this)']")
if dynamic_button.text == "START":
    dynamic_button.click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH,"//button[@onclick='toggleButton(this)']"), "STOP"))
    print("Button text changed to 'Stop'")

else:
    dynamic_button.click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//button[@onclick='toggleButton(this)']"), "START"))
    print("Button text changed to 'Start'")



# Alerts and Popups

driver.find_element(By.XPATH,"//button[@id='alertBtn']").click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()
time.sleep(5)

driver.find_element(By.XPATH,"//button[@id='confirmBtn']").click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()
wait.until(EC.text_to_be_present_in_element((By.XPATH, "//p[@id='demo']"), "You pressed OK!"))
time.sleep(5)

driver.find_element(By.XPATH,"//button[@id='confirmBtn']").click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.dismiss()
wait.until(EC.text_to_be_present_in_element((By.XPATH, "//p[@id='demo']"), "You pressed Cancel!"))


driver.find_element(By.XPATH,"//button[@id='promptBtn']").click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.send_keys("Laraib")
alert.accept()
wait.until(EC.text_to_be_present_in_element((By.XPATH, "//p[@id='demo']"), "Hello Laraib! How are you today?"))


# Open New Tab

# Store the current number of tabs
initial_tabs = driver.window_handles
initial_tab_count = len(initial_tabs)

driver.find_element(By.XPATH,"//button[text()='New Tab']").click()

# Wait briefly to allow the new tab to open
time.sleep(2)  # You can replace this with WebDriverWait for more reliability

# Get updated list of tabs
new_tabs = driver.window_handles
new_tab_count = len(new_tabs)
print("New Id:", new_tabs)

# Verify if a new tab is opened
if new_tab_count > initial_tab_count:
    print("✅ New tab successfully opened with count", new_tab_count, ".")
    # # Verify title
    # driver.switch_to.window(new_tabs[3])
    # expected_title = "SDET-QA Blog"
    # actual_title = driver.title
    #
    # if actual_title == expected_title:
    #     print("✅ New tab title is correct:", actual_title)
    # else:
    #     print(f"❌ New tab title is incorrect. Found: {actual_title}")

    expected_title = "SDET-QA Blog"
    all_tabs = driver.window_handles

    # Loop through all tabs
    for tab in all_tabs:
        driver.switch_to.window(tab)
        if driver.title == expected_title:
            print(f"✅ Switched to tab with title: {expected_title}")
            break
    else:
        print(f"❌ No tab found with title: {expected_title}")

else:
    print(f"❌ New tab was not opened and the count is ({initial_tab_count}).")


driver.switch_to.window(new_tabs[0])

# Popup

#
# before_popup = driver.window_handles
# before_popup_count = len(before_popup)
#
# driver.find_element(By.XPATH,"//button[@id='PopUp']").click()
# after_popup = driver.window_handles
# after_popup_count = len(after_popup)
#
# if after_popup_count > before_popup_count:
#     print("✅ Popup successfully opened with count", after_popup_count, ".")
#     popup_expected_title = "Selenium"
#     all_tabs = driver.window_handles
#
#     # Loop through all tabs
#     for tab in all_tabs:
#         driver.switch_to.window(tab)
#         if driver.title == popup_expected_title:
#             print(f"✅ Switched to Popup tab with title: {popup_expected_title}")
#             break
#     else:
#         print(f"❌ No Popup tab found with title: {popup_expected_title}")
# else:
#     print(f"❌ Popup was not opened and the count is ({before_popup_count}).")




existing_windows = driver.window_handles
current_window = driver.current_window_handle

driver.find_element(By.XPATH,"//button[@id='PopUp']").click()

# wait.until(
#     lambda d: len(d.window_handles) > len(existing_windows)
# )
# new_windows = driver.window_handles
# new_window = list(set(new_windows) - set(existing_windows))[0]
# driver.switch_to.window(new_window)
# popup_title = driver.title
# print("New Popup Title:", popup_title)

# Wait briefly to allow popups to open
time.sleep(2)

# Step 3: Get updated window handles
new_windows = driver.window_handles

# Step 4: Identify only the new popup windows
popup_windows = list(set(new_windows) - set(existing_windows))

# Step 5: Loop through each new popup and print its title
popup_titles = []
for handle in popup_windows:
    driver.switch_to.window(handle)
    popup_titles.append(driver.title)
    driver.close()

# Print all new popup titles
print("New popup window titles:")
for title in popup_titles:
    print("-", title)

# Optional: Switch back to original window
# driver.switch_to.window(existing_windows[0])
driver.switch_to.window(current_window)


#  Mouse Action


# Locate the element to hover over
mouse_hover = driver.find_element(By.XPATH, "//button[@class='dropbtn']")  # Replace with your XPath

# Create ActionChains object
actions = ActionChains(driver)

# Perform mouse hover
hover = actions.move_to_element(mouse_hover)
sub_menu = driver.find_element(By.XPATH,"//a[text()='Mobiles']")
# time.sleep(5)
# hover.perform()
hover.click(sub_menu).perform()




# Input form
field1 = driver.find_element(By.XPATH,"//input[@id='field1']")
field1.send_keys("Amet et impedit aliquam")
field2 = driver.find_element(By.XPATH,"//input[@id='field2']")
field2.send_keys("Laraib Khalid")

time.sleep(5)

double_click_button = driver.find_element(By.XPATH,"//button[text()='Copy Text']")
actions.double_click(double_click_button).perform()

data1 = field1.get_attribute("value")
data2 = field2.get_attribute("value")

if data1 == data2:
    print(f"✅ Input 1 '{data1}' and Input 2 '{data2}' have the same text.")
else:
    print("❌ Input 1 and Input 2 have different text.")


drag = driver.find_element(By.XPATH,"//div[@id='draggable']")
drop = driver.find_element(By.XPATH,"//div[@id='droppable']")
actions.drag_and_drop(drag,drop).perform()

drop_text = driver.find_element(By.XPATH,"//div[@id='droppable']//p").text
if drop_text == "Dropped!":
    print("✅ Drag and Drop was successful.")
else:
    print("❌ Drag and Drop was not successful.")


# Locate both slider handles
handles = driver.find_elements(By.CLASS_NAME, "ui-slider-handle")
min_handle = handles[0]
max_handle = handles[1]

# Move min handle to the right (e.g., 40px)
actions.click_and_hold(min_handle).move_by_offset(40, 0).release().perform()
time.sleep(1)

# Move max handle to the left (e.g., -60px)
actions.click_and_hold(max_handle).move_by_offset(-60, 0).release().perform()



# Scroll dropdown
dropdown = driver.find_element(By.XPATH,"//input[@id='comboBox']")
dropdown.click()
wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@id='dropdown']")))
dropdown_option = driver.find_element(By.XPATH,"//div[text()='Item 18']")
# actions.move_to_element(dropdown_option).perform()
time.sleep(5)
dropdown_option.click()


driver.find_element(By.LINK_TEXT,"Lenovo").click()

driver.find_element(By.LINK_TEXT, "Errorcode 403").click()


driver.switch_to.new_window()
driver.get("https://letcode.in/frame")
time.sleep(20)

# driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
# driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
# driver.find_element(By.XPATH, "//button[@type='submit']").click()