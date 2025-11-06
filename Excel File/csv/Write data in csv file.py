import os
import csv

# Step 1: Create folder if it doesn't exist
folder_path = "Excel_CSV"
os.makedirs(folder_path, exist_ok=True)

# Step 2: Define CSV file path
file_path = os.path.join(folder_path, "Test_Data.csv")

# Step 3: Define your test data
data = [
    ["Username", "Password", "Expected"],
    ["admin123", "admin123", "Failure"],
    ["user1", "wrong123", "Failure"],
    ["admin", "admin123","Success"]
]

# Step 4: Write data into CSV file
with open(file_path, mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"✅ CSV file created successfully at: {file_path}")
