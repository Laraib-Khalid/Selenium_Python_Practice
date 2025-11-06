# ------------------------ Create Excel File: TestData.xlsx ------------------------
import os
from openpyxl import Workbook

# Create a new Excel workbook and select the active worksheet
workbook = Workbook()
sheet = workbook.active

# Rename the sheet for clarity
sheet.title = "Login_Data"

# Write the header row
sheet.append(["Username", "Password", "Expected Result"])

# Write test data rows
sheet.append(["user1", "wrong123", "Failure"])
sheet.append(["admin", "admin", "Failure"])
sheet.append(["Admin", "admin123", "Success"])

print(os.getcwd())
os.makedirs("Excel", exist_ok=True)

# Save the workbook as TestData.xlsx in the current directory
workbook.save("Excel/Test_Data.xlsx")

print("✅ Excel file 'Test_Data.xlsx' created successfully with test data.")
