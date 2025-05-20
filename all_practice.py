import time
import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

# Launch the Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open the practice website
driver.get("https://testautomationpractice.blogspot.com/")
print("Website Title is:", driver.title)

# Wait for the header to be visible and verify it
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[@class='title']")))
header_text = driver.find_element(By.XPATH, "//h1[@class='title']")
print("Is Dashboard displayed?", header_text.is_displayed())
print("Header Text is:", header_text.text)
time.sleep(2)

# --- Fill out the Form ---

# Enter Name
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Laraib Khalid")

# Enter Email
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("laraib.khalid@pk.com")

# Enter Phone
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("1234567890")

# Enter Comment/Description
driver.find_element(By.XPATH, "//textarea[@id='textarea']").send_keys("Automation Testing")

# --- Select Gender Radio Button ---

# Find all gender radio buttons
gender_radiobutton = driver.find_elements(By.XPATH, "//input[@name='gender']")
print("Gender radio buttons found:", len(gender_radiobutton))

# Select 'Female' gender if not already selected
for radio in gender_radiobutton:
    if radio.get_attribute("value").lower() == "female":
        if not radio.is_selected():
            radio.click()
            print("Female gender selected.")
        break

# --- Select Days Checkboxes ---

# Find all day checkboxes
days_checkbox = driver.find_elements(By.XPATH, "//div[@class='form-group']//input[@type='checkbox']")
print("Days checkboxes found:", len(days_checkbox))

# Define the days you want to select
days_to_select = ["monday", "wednesday", "friday"]

# Loop through checkboxes and select specified days
for checkbox in days_checkbox:
    value = checkbox.get_attribute("value").lower()
    if value in days_to_select:
        if not checkbox.is_selected():
            checkbox.click()
            print(f"{value.capitalize()} checkbox selected.")

# --- Handle Single-Select Dropdown ---

# Locate the country dropdown
dropdown = driver.find_element(By.XPATH, "//select[@id='country']")
select = Select(dropdown)

# Select by value
select.select_by_value("uk")
print("Country selected (by value):", select.first_selected_option.text)

# Select by visible text
select.select_by_visible_text("Germany")
print("Country selected (by visible text):", select.first_selected_option.text)

# Select by index
select.select_by_index(6)
print("Country selected (by index):", select.first_selected_option.text)

# --- Handle Multi-Select Dropdown ---

# Locate multi-select dropdown for colors
multi_select_dropdown = driver.find_element(By.XPATH, "//select[@id='colors']")
multi_select = Select(multi_select_dropdown)

# Check if the dropdown allows multiple selection
if multi_select.is_multiple:
    # Select multiple colors
    multi_select.select_by_visible_text("White")
    multi_select.select_by_visible_text("Green")
    multi_select.select_by_visible_text("Blue")

    selected_colors = [option.text for option in multi_select.all_selected_options]
    print("Colors selected:", ", ".join(selected_colors))
else:
    print("This is not a multi-select dropdown.")

time.sleep(2)

# Deselect one color ('Green') and display remaining selected colors
multi_select.deselect_by_visible_text("Green")
remaining_colors = [option.text for option in multi_select.all_selected_options]
print("Colors selected after deselecting Green:", ", ".join(remaining_colors))


# --- Handle Dropdown: Check if Sorted and Select All if Multi-Select ---

# Locate the dropdown element by ID (replace 'animals' with actual if needed)
dropdown_element = driver.find_element(By.ID, "animals")
select = Select(dropdown_element)

# Get text of all options in dropdown
options_text = [option.text for option in select.options]

# Check if dropdown options are sorted alphabetically
if options_text == sorted(options_text):
    print("Dropdown options are sorted.")

    # If dropdown is multi-select, select all options
    if select.is_multiple:
        for option in select.options:
            select.select_by_visible_text(option.text)
            print(f"Selected: {option.text}")
    else:
        print("Dropdown is not multi-select. Cannot select all.")
else:
    print("Dropdown options are NOT sorted. Nothing selected.")

# --- Interact with jQuery Calendar (First Datepicker) ---

# Click to open the datepicker
driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

# Navigate to the previous month
driver.find_element(By.XPATH, "//a[@title='Prev']").click()

# Select the 23rd day of the previous month
driver.find_element(By.XPATH, "//a[@data-date='23']").click()

# --- Interact with jQuery Calendar (Second Datepicker with Year/Month Select) ---

# Click to open the calendar input
driver.find_element(By.XPATH, "//input[@id='txtDate']").click()

# Select Month = March
select_month_dropdown = driver.find_element(By.XPATH, "//select[@aria-label='Select month' and @class = 'ui-datepicker-month']")
select_month = Select(select_month_dropdown)
select_month.select_by_visible_text("Mar")

# Select Year = 2018
select_year_dropdown = driver.find_element(By.XPATH, "//select[@aria-label='Select year' and @class = 'ui-datepicker-year']")
select_year = Select(select_year_dropdown)
select_year.select_by_visible_text("2018")

# Select Day = 21
driver.find_element(By.XPATH, "//td[@data-handler='selectDay']//a[@data-date='21']").click()

# --- Enter Date Range and Validate Result Message ---

# Define start and end date strings
start_date_str = "12/01/1998"
end_date_str = "12/01/2025"

# Locate and fill start date field
start_input = driver.find_element(By.ID, "start-date")
start_input.clear()
start_input.send_keys(start_date_str.replace("/", ""))  # format: MMDDYYYY

# Locate and fill end date field
end_input = driver.find_element(By.ID, "end-date")
end_input.clear()
end_input.send_keys(end_date_str.replace("/", ""))  # format: MMDDYYYY

# Click Submit button to calculate date range
driver.find_element(By.XPATH, "//button[@class='submit-btn']").click()

# Wait for the result message to become visible
wait = WebDriverWait(driver, 10)
result = wait.until(EC.visibility_of_element_located((By.ID, "result")))

# Get and print the result text
result_text = result.text
print("Displayed Result:", result_text)

# Validate the result contains expected phrase
if "You selected a range of" in result_text:
    print("PASS: Text contains expected phrase.")

    # Extract number of days from result text using regex
    match = re.search(r"(\d+)\s+days", result_text)
    if match:
        displayed_days = int(match.group(1))

        # Calculate actual number of days between two dates
        start_dt = datetime.strptime(start_date_str, "%m/%d/%Y")
        end_dt = datetime.strptime(end_date_str, "%m/%d/%Y")
        actual_days = (end_dt - start_dt).days

        # Compare calculated and displayed day count
        if displayed_days == actual_days:
            print(f"PASS: Displayed days ({displayed_days}) match actual difference ({actual_days}).")
        else:
            print(f"FAIL: Displayed days ({displayed_days}) do NOT match actual ({actual_days}).")
    else:
        print("FAIL: Could not extract number of days from result.")
else:
    print("FAIL: Expected message not found.")

# --- Upload Single File ---

# Wait until single file form is present
wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@id='singleFileForm']")))

# Locate the single file input and upload a file by providing full path
upload_single_input = driver.find_element(By.XPATH, "//input[@id='singleFileInput']")
file_path = r"C:\Users\LaraibKhalid\Downloads\monthly-budget-expenses-spreadsheet-within-business-income-and-expense-spreadsheet-with-template-sheet-to.jpg"
upload_single_input.send_keys(file_path)

# Click the button to upload single file
driver.find_element(By.XPATH, "//button[text()='Upload Single File']").click()

# --- Upload Multiple Files ---

# Locate the multi-file input field
upload_multiple_input = driver.find_element(By.XPATH, "//input[@id='multipleFilesInput']")

# Define a list of file names to be uploaded
file_names = [
    "WhatsApp Image 2025-04-24 at 4.37.27 PM.jpeg",
    "WhatsApp Image 2025-04-24 at 4.37.26 PM (1).jpeg",
    "monthly-budget-expenses-spreadsheet-within-business-income-and-expense-spreadsheet-with-template-sheet-to.jpg"
]

# Convert list of names to absolute paths
file_paths = [rf"C:\Users\LaraibKhalid\Downloads\{file_name}" for file_name in file_names]

# Join file paths with newline separator for multi-upload
upload_multiple_input.send_keys("\n".join(file_paths))

# Click button to upload multiple files
driver.find_element(By.XPATH, "//button[text()='Upload Multiple Files']").click()


# ------------------------ Table Parsing - BookTable ------------------------

# Locate all table rows under BookTable
rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")

# Loop through each row to extract data
for row in rows:
    # If the row contains headers (th elements), print headers
    header_row = row.find_elements(By.TAG_NAME, "th")
    if header_row:
        header_values = [header.text for header in header_row]
        print("Headers:", header_values)
    else:
        # Else, it's a data row (td elements), extract and print values
        cells = row.find_elements(By.TAG_NAME, "td")
        values = [cell.text for cell in cells]
        print("Row:", values)

# Print specific cell value: 3rd row, 2nd column
specific_cell = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[3]/td[2]")
print("Specific Cell Value:", specific_cell.text)

# Extract all 2nd column values from rows (skip header rows)
second_column_values = [
    row.find_elements(By.TAG_NAME, "td")[1].text
    for row in rows if len(row.find_elements(By.TAG_NAME, "td")) > 1
]
print("Second Column Values:", second_column_values)

# Extract all 3rd column values (using XPath)
third_column_elements = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/td[3]")
third_column_values = [elem.text for elem in third_column_elements]
print("Third Column Values:", third_column_values)

# Get unique/distinct values from the 3rd column
distinct_third_column_values = list(set(third_column_values))
print("Distinct Third Column Values:", distinct_third_column_values)


# ------------------------ Dynamic Table Handling - taskTable ------------------------

# Locate all rows under taskTable
dynamic_rows = driver.find_elements(By.XPATH, "//table[@id='taskTable']/tbody/tr")

# Extract and print each dynamic row
for dynamic_row in dynamic_rows:
    dynamic_cells = dynamic_row.find_elements(By.TAG_NAME, "td")
    dynamic_values = [dynamic_cell.text for dynamic_cell in dynamic_cells]
    print("Dynamic Row:", dynamic_values)


# ------------------------ Pagination and Product Table ------------------------

# Click on page 3 of the pagination
driver.find_element(By.XPATH, "//ul[@id='pagination']//li/a[text()='3']").click()

# Locate all rows of productTable
productTable_rows = driver.find_elements(By.XPATH, "//table[@id='productTable']//tr")

# Loop and print headers or row data
for productTable_row in productTable_rows:
    productTable_header_row = productTable_row.find_elements(By.TAG_NAME, "th")
    if productTable_header_row:
        productTable_header_values = [header.text for header in productTable_header_row]
        print("Headers:", productTable_header_values)
    else:
        productTable_cells = productTable_row.find_elements(By.TAG_NAME, "td")
        productTable_values = [cell.text for cell in productTable_cells]
        print("Row:", productTable_values)

# Select checkboxes in specific rows
driver.find_element(By.XPATH, "//table[@id='productTable']//tr[3]//input[@type='checkbox']").click()
driver.find_element(By.XPATH, "//table[@id='productTable']//tr[5]//input[@type='checkbox']").click()


# ------------------------ Input Fields and Button Clicks ------------------------

# Enter text and click buttons
driver.find_element(By.XPATH, "//input[@id='input1']").send_keys("Laraib")
driver.find_element(By.XPATH, "//button[@id='btn1']").click()
driver.find_element(By.XPATH, "//input[@id='input2']").send_keys("Khalid")
driver.find_element(By.XPATH, "//button[@id='btn2']").click()
driver.find_element(By.XPATH, "//input[@id='input3']").send_keys("Masood")
driver.find_element(By.XPATH, "//button[@id='btn3']").click()


# ------------------------ Wikipedia Search and Tab Switching ------------------------

# Perform search on Wikipedia and click result
driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("Python")
driver.find_element(By.XPATH, "//input[@class='wikipedia-search-button']").click()
wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='wikipedia-search-results']")))
time.sleep(2)
driver.find_element(By.XPATH, "//a[text()='Python (programming language)']").click()
time.sleep(5)

# Switch back to original tab
tabs = driver.window_handles
driver.switch_to.window(tabs[0])


# ------------------------ Open New Window ------------------------

# Open a new window and go to drag and drop demo site
driver.switch_to.new_window('window')
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
time.sleep(2)

# Switch back to original window
windows = driver.window_handles
driver.switch_to.window(windows[0])


# ------------------------ Toggle Button Test ------------------------

# Toggle button between START and STOP states
dynamic_button = driver.find_element(By.XPATH, "//button[@onclick='toggleButton(this)']")
if dynamic_button.text == "START":
    dynamic_button.click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//button[@onclick='toggleButton(this)']"), "STOP"))
    print("Button text changed to 'Stop'")
else:
    dynamic_button.click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//button[@onclick='toggleButton(this)']"), "START"))
    print("Button text changed to 'Start'")


# ------------------------ JavaScript Alerts ------------------------

# Handle simple alert
driver.find_element(By.XPATH, "//button[@id='alertBtn']").click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()

# Handle confirmation alert - Accept
driver.find_element(By.XPATH, "//button[@id='confirmBtn']").click()
wait.until(EC.alert_is_present())
driver.switch_to.alert.accept()
wait.until(EC.text_to_be_present_in_element((By.XPATH, "//p[@id='demo']"), "You pressed OK!"))

# Handle confirmation alert - Dismiss
driver.find_element(By.XPATH, "//button[@id='confirmBtn']").click()
wait.until(EC.alert_is_present())
driver.switch_to.alert.dismiss()
wait.until(EC.text_to_be_present_in_element((By.XPATH, "//p[@id='demo']"), "You pressed Cancel!"))

# Handle prompt alert
driver.find_element(By.XPATH, "//button[@id='promptBtn']").click()
wait.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.send_keys("Laraib")
alert.accept()
wait.until(EC.text_to_be_present_in_element((By.XPATH, "//p[@id='demo']"), "Hello Laraib! How are you today?"))


# ------------------------ New Tab Verification ------------------------

# Store current tab count
initial_tabs = driver.window_handles
initial_tab_count = len(initial_tabs)

# Click to open a new tab
driver.find_element(By.XPATH, "//button[text()='New Tab']").click()
time.sleep(2)

# Compare new tab count
new_tabs = driver.window_handles
if len(new_tabs) > initial_tab_count:
    print("✅ New tab successfully opened.")

    # Switch and verify tab title
    expected_title = "SDET-QA Blog"
    for tab in new_tabs:
        driver.switch_to.window(tab)
        if driver.title == expected_title:
            print(f"✅ Switched to tab with title: {expected_title}")
            break
    else:
        print(f"❌ No tab found with title: {expected_title}")
else:
    print("❌ New tab was not opened.")


# Switch back to original tab
driver.switch_to.window(initial_tabs[0])


# ------------------------ Popup Window Handling ------------------------


# Capture current window handle and open popup
existing_windows = driver.window_handles
current_window = driver.current_window_handle

driver.find_element(By.XPATH, "//button[@id='PopUp']").click()
time.sleep(2)

# Detect newly opened windows
new_windows = driver.window_handles
popup_windows = list(set(new_windows) - set(existing_windows))

# Loop through each popup window and print its title
popup_titles = []
for handle in popup_windows:
    driver.switch_to.window(handle)
    popup_titles.append(driver.title)
    driver.close()

print("New popup window titles:")
for title in popup_titles:
    print("-", title)

# Switch back to original window
driver.switch_to.window(current_window)


# ------------------------ Mouse Actions - Hover & Click ------------------------

# Hover over dropdown menu and click "Mobiles"
mouse_hover = driver.find_element(By.XPATH, "//button[@class='dropbtn']")
actions = ActionChains(driver)
sub_menu = driver.find_element(By.XPATH, "//a[text()='Mobiles']")
actions.move_to_element(mouse_hover).click(sub_menu).perform()


# ------------------------ Double Click to Copy Text ------------------------

# Enter text in fields and perform double click to copy
field1 = driver.find_element(By.XPATH, "//input[@id='field1']")
field1.send_keys("Amet et impedit aliquam")

field2 = driver.find_element(By.XPATH, "//input[@id='field2']")
field2.send_keys("Laraib Khalid")

double_click_button = driver.find_element(By.XPATH, "//button[text()='Copy Text']")
actions.double_click(double_click_button).perform()

# Validate copied text
data1 = field1.get_attribute("value")
data2 = field2.get_attribute("value")

if data1 == data2:
    print(f"✅ Input 1 '{data1}' and Input 2 '{data2}' have the same text.")
else:
    print("❌ Input 1 and Input 2 have different text.")


# ------------------------ Drag and Drop Action ------------------------

drag = driver.find_element(By.XPATH, "//div[@id='draggable']")
drop = driver.find_element(By.XPATH, "//div[@id='droppable']")
actions.drag_and_drop(drag, drop).perform()

# Confirm drag and drop result
drop_text = drop.find_element(By.TAG_NAME, "p").text
if drop_text == "Dropped!":
    print("✅ Drag and Drop was successful.")
else:
    print("❌ Drag and Drop was not successful.")


# ------------------------ Slider Drag Operation ------------------------

# Locate slider handles
handles = driver.find_elements(By.CLASS_NAME, "ui-slider-handle")
min_handle = handles[0]
max_handle = handles[1]

# Move handles to desired position
actions.click_and_hold(min_handle).move_by_offset(40, 0).release().perform()
time.sleep(1)
actions.click_and_hold(max_handle).move_by_offset(-60, 0).release().perform()


# ------------------------ Dropdown Option Selection ------------------------

# Locate the dropdown input box and click to open the dropdown list
dropdown = driver.find_element(By.XPATH, "//input[@id='comboBox']")
dropdown.click()

# Wait until the dropdown options container becomes visible
wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='dropdown']")))

# Locate the specific dropdown option (e.g., "Item 65")
dropdown_option = driver.find_element(By.XPATH, "//div[text()='Item 65']")

# Scroll to the dropdown option using mouse movement to make sure it's in view
actions.move_to_element(dropdown_option).perform()
time.sleep(5)  # Pause for visibility or animation delay

# Click the desired dropdown option
dropdown_option.click()


# Pause to observe final state
time.sleep(20)
