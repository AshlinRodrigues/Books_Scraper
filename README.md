Books to Scrape — Data Extraction and Analysis Project

 User Story

As a **data analyst**, I want to scrape book details such as **Title, Price, Rating, Availability**, and **Product URL** from [Books to Scrape](http://books.toscrape.com/), so that I can analyze book trends, pricing, and stock availability.



## Features Implemented

### 1. Web Scraping
- Extracts **all books** from the site (~1001 books across 50 pages)
- Extracted fields:
  - `Title`
  - `Price`
  - `Rating (1–5)`
  - `Availability` (In Stock / Out of Stock)
  - `Product URL`

### 2.Data Storage
- Data saved in a **CSV file**: `books_data.csv`
- Format:  
  `Title, Price, Rating, Availability, URL`

### 3. Error Handling
- Skips and logs missing data fields
- Handles network or HTTP issues (e.g., 404, 503) using `try-except`
- Errors saved in `scraper_errors.log`

### 4.  Testing
**Manual test cases** located in:
- `tests/test_cases.py`

Test Cases:
-  CSV file is created
-  Correct headers
- Valid book count (1001)
-  Duplicate check on URLs
-  Detect missing or "N/A" fields

### 5. Data Analysis
Using `analyze_books.py`:
Stored under `additional/` folder
- Total book count
- Price statistics
- Ratings distribution
- Stock availability
- Top 5 most expensive books

### 6. Data Visualization
Using `visualize_books.py`:
Stored under `additional/` folder
- Interactive bar charts:
  - Rating counts
  - Stock status
  - Price distribution
  - Top expensive books
- Navigate charts using **Next** and **Back** buttons



##  Folder Structure
```
Books_Scraper/
|
├── additional/                 ←  Analysis and visualization scripts
│   ├── analyze_books.py
│   └── visualize_books.py
│
├── images/                     ←  Saved graphs/images
│   ├── avg_price_per_rating.png
│   ├── price_distribution.png
│   ├── rating_distribution.png
│   └── top_10_expensive_books.png
│
├── tests/                      ←  All test-related scripts
│   ├── test_books_scraper.py
│   ├── test_cases.py
│   └── verify_count.py
│
├── venv/                       ← virtual environment
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   ├── share/
│   └── pyvenv.cfg
│
├── books_data.csv             ← Final scraped data (CSV file)
├── books_scraper.py           ←  Main web scraping script
├── README.md                  ←  Project description and documentation
├── requirements.txt           ←  All required libraries for setup
└── scraper_errors.log         ←  Logged errors from the scraping process

```
