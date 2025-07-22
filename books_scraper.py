import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin
import logging
import re

#   Setup logging
logging.basicConfig(
    filename='scraper_errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

BASE_URL = "http://books.toscrape.com/"
seen_urls = set()  # To track already scraped URLs

#   Step 1: Create CSV and write header
with open("books_data.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Rating", "Availability", "URL"])

#   Step 2: Use a session for efficient scraping
with requests.Session() as session:
    current_url = BASE_URL

    while current_url:
        try:
            response = session.get(current_url, timeout=10)
            print(f"Scraping: {current_url} — Status Code: {response.status_code}")
        except requests.RequestException as net_err:
            logging.error(f"Network error fetching {current_url}: {net_err}")
            print("  Network error. Check your connection or the website.")
            break

        if response.status_code != 200:
            logging.error(f"HTTP error {response.status_code} on {current_url}")
            print(f"  Failed to load page. Status: {response.status_code}")
            break

        try:
            soup = BeautifulSoup(response.text, "html.parser")
            books = soup.find_all("article", class_="product_pod")
            print(f"Found {len(books)} books on this page.")
        except Exception as parse_err:
            logging.error(f"Parsing error on {current_url}: {parse_err}")
            print("  Could not parse this page.")
            break

        #   Step 3: Append book data to CSV
        with open("books_data.csv", mode="a", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)

            for book in books:
                try:
                    partial_url = book.h3.a["href"]
                    full_url = urljoin(current_url, partial_url)

                    if full_url in seen_urls:
                        continue  # Skip duplicates
                    seen_urls.add(full_url)

                    title = book.h3.a.get("title", "N/A")

                    price_tag = book.find("p", class_="price_color")
                    raw_price = price_tag.text if price_tag else "£0"
                    price = re.sub(r"[^\d.]", "", raw_price)  # Removes £, Â, etc.

                    availability_tag = book.find("p", class_="instock availability")
                    availability = availability_tag.text.strip() if availability_tag else "N/A"

                    rating_class = book.find("p", class_="star-rating")
                    rating_text = rating_class["class"][1] if rating_class and len(rating_class["class"]) > 1 else "Zero"
                    rating_dict = {"Zero": 0, "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
                    rating = rating_dict.get(rating_text, 0)

                    writer.writerow([title, price, rating, availability, full_url])

                except Exception as e:
                    logging.error(f"Error scraping book on {current_url}: {e}")
                    print(" Skipped a book due to error.")
                    continue

        #   Step 4: Move to next page
        next_button = soup.find("li", class_="next")
        if next_button:
            next_page_url = next_button.a["href"]
            current_url = urljoin(current_url, next_page_url)
        else:
            print("  No more pages. Finished scraping.")
            break

print("  All unique book data saved to books_data.csv.")
print(" Any issues were logged in scraper_errors.log.")

