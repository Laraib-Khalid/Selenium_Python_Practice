import csv


class CSV_Excel_Utils:
    def __init__(self, file_path):
        self.file_path = file_path

    # Function to write data into a CSV file
    def write_csv(self,data, show_message=True):
        """
        Write data to a CSV file.
        Args:
            file_path (str): Path where CSV will be saved.
            data (list of lists): Data to be written to the CSV file.
        """
        with open(self.file_path, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)
        if show_message:
            print(f"✅ Data written successfully to {self.file_path}")


    # Function to read data from a CSV file
    def read_csv(self):
        """
        Read data from a CSV file.
        Args:
            file_path (str): Path of the CSV file.
        Returns:
            list of lists: Data read from the CSV file.
        """
        with open(self.file_path, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            data = list(reader)
        return data


    # Read specific cell (row, col)
    def read_cell(self, row, col):
        """Read a specific cell value (1-based index)."""
        data = self.read_csv()
        return data[row - 1][col - 1]

    # Write to specific cell
    # def write_cell(self, row, col, value):
    #     """Write a value to a specific cell (1-based index)."""
    #     data = self.read_csv()
    #     data[row - 1][col - 1] = value
    #     self.write_csv(data)

    def write_cell(self, row, col, value):
        """Write a value to a specific cell (1-based index)."""
        data = self.read_csv()

        # Ensure the row exists
        while len(data) < row:
            data.append([])

        # Ensure the column exists in that row
        while len(data[row - 1]) < col:
            data[row - 1].append("")

        # Now safely assign value
        data[row - 1][col - 1] = value

        # Write without printing success message
        self.write_csv(data, show_message=False)

    # Function to get total rows automatically (no need to pass data)
    def get_max_rows(self):
        """Return total number of rows in the CSV file."""
        data = self.read_csv()
        return len(data)

    # Function to get total columns automatically (no need to pass data)
    def get_max_columns(self):
        """Return total number of columns in the CSV file."""
        data = self.read_csv()
        return len(data[0]) if data else 0

