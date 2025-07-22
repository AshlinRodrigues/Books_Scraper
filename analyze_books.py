import pandas as pd

#  Step 1: Load the CSV file
df = pd.read_csv("books_data.csv")

#  Step 2: Clean Price Column
# Convert to string in case it's not already, remove £ and junk chars, convert to float
df["Price"] = df["Price"].astype(str).str.replace(r"[^\d.]", "", regex=True).astype(float)

#   Step 3: Summary Stats
print("\n TOTAL BOOKS:", len(df))
print(" COLUMNS:", df.columns.tolist())

#   Step 4: Price Summary
print("\n PRICE SUMMARY:")
print(df["Price"].describe())

#   Step 5: Rating Distribution
print("\n RATING COUNTS:")
print(df["Rating"].value_counts().sort_index())

#   Step 6: Stock Availability Info
print("\n STOCK AVAILABILITY:")
print(df["Availability"].value_counts())

#   Step 7: Average Book Price
avg_price = round(df["Price"].mean(), 2)
print(f"\n AVERAGE BOOK PRICE: £{avg_price}")

#   Step 8: Most Expensive Books
print("\n TOP 5 MOST EXPENSIVE BOOKS:")
print(df.sort_values(by="Price", ascending=False).head(5)[["Title", "Price", "Rating"]])

#   Optional: Cheapest Books
print("\n BOTTOM 5 CHEAPEST BOOKS:")
print(df.sort_values(by="Price", ascending=True).head(5)[["Title", "Price", "Rating"]])
