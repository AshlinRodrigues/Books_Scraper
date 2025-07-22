import csv

with open("books_data.csv", newline='', encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    rows = list(reader)
    urls = [row[4] for row in rows]

print("  Total Books:", len(rows))
print("  Unique URLs:", len(set(urls)))
