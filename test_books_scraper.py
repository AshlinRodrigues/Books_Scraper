import unittest
import os
import csv

class TestBookScraper(unittest.TestCase):

    def setUp(self):
        self.file_path = "books_data.csv"

    def test_file_exists(self):
        """Test 1: Check if the CSV file was created."""
        self.assertTrue(os.path.exists(self.file_path), "CSV file not found.")

    def test_file_extension(self):
        """Test 2: File should have .csv extension."""
        self.assertTrue(self.file_path.endswith(".csv"), "File is not a .csv file.")

    def test_csv_header(self):
        """Test 3: CSV should contain correct headers."""
        with open(self.file_path, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            expected_headers = ["Title", "Price", "Rating", "Availability", "URL"]
            self.assertEqual(headers, expected_headers, "CSV headers do not match.")

    def test_data_rows_present(self):
        """Test 4: At least one book entry should be present."""
        with open(self.file_path, newline='', encoding='utf-8') as file:
            reader = list(csv.reader(file))
            self.assertGreater(len(reader), 1, "CSV contains no book data.")

    def test_data_fields_complete(self):
        """Test 5: No missing fields in data rows."""
        with open(self.file_path, newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                self.assertEqual(len(row), 5, f"Row has incorrect number of fields: {row}")
                for field in row:
                    self.assertNotEqual(field.strip(), "", f"Empty field in row: {row}")

if __name__ == "__main__":
    unittest.main()
