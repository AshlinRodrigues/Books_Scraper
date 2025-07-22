import csv
import os

CSV_FILE = "books_data.csv"

#   Test Case 1: Check if CSV file exists
print("\n--- Test Case 1: File Exists ---")
if os.path.exists(CSV_FILE):
    print("  CSV file found.")
else:
    print(" CSV file missing!")
    exit()

#   Open the file and load data safely
with open(CSV_FILE, newline='', encoding="utf-8") as file:
    reader = csv.reader(file)
    headers = next(reader)
    rows = list(reader)  # Now it's inside the open block

#   Test Case 2: Check column structure
print("\n--- Test Case 2: Column Structure ---")
expected_headers = ["Title", "Price", "Rating", "Availability", "URL"]
if headers == expected_headers:
    print("  Columns are correct.")
else:
    print(" Columns are incorrect.")
    print("Found:", headers)

#   Test Case 3: Book Count
print("\n--- Test Case 3: Book Count ---")
print("Total books:", len(rows))
if len(rows) == 1001:
    print("  All 1001 books scraped.")
elif len(rows) > 1001:
    print(" More than 1001 books (possible duplicates).")
else:
    print("Less than 1001 books (some may be missing).")

#   Test Case 4: Unique Book URLs
print("\n--- Test Case 4: Unique Book URLs ---")
urls = [row[4] for row in rows]
if len(urls) == len(set(urls)):
    print("  All book URLs are unique.")
else:
    print(" Duplicate book entries found!")

#   Test Case 5: Missing Data Fields
print("\n--- Test Case 5: Missing Data Fields ---")
missing_count = 0
for row in rows:
    if "" in row or "N/A" in row:
        missing_count += 1
print(f"Books with missing data: {missing_count}")
if missing_count == 0:
    print("  All fields present.")
else:
    print(" Some books have missing fields.")
