# NOTE: I'M SCRAPING DATA FROM USERS' (JDCarrr99/lists/OL207808L/New_Books) PERSONAL PAGES SINCE WHEN I WAS TRYING TO SCRAP DATA PER SUBJECT (SCIENCE FICTION, etc..) SERVICE WAS ALWAYS UNAVAILABLE RETURNING TIMEOUTS, THEREFORE THIS WAS THE WAY

# 📚 OpenLibrary Book Scraper

This Python project is a web scraper built to collect book data from [OpenLibrary.org](https://openlibrary.org). It
fetches and parses content with Python, respecting Terms of Service & robots.txt rules, rate limits requests, and book
information using BeautifulSoup.

---

## 🧠 What it does

- Scrapes books from a specific users' page on OpenLibrary (like science fiction, art, etc.)
- Collects details such as title, author, book URL, and cover image
- Saves the data in **JSON** and **CSV** formats
- Provides easy methods to:
    - Paginate through the book pages & get up to x books
    - Filter books by keywords in the title
    - Get all unique authors
    - Get authors who have written >= x books
    - Data visualization with matplotlib
    - More to be added...
- Handles errors gracefully (e.g. missing data, connection issues)
- Follows proper object-oriented design (OOP principles)
- Tests main functionality with unit tests

---

## 🛠️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/giorgigagnidze16/data-scraping.git
cd data-scraping


python -m venv venv
source venv/bin/activate 

pip install -r requirements.txt

```

## 🧩 Features

OOP Design:

Book class for book data

BookCollection class for managing lists of books

OpenLibraryScraper for all scraping logic

BeautifulSoup4:

Uses multiple selection techniques

DOM navigation for nested elements

Rate Limiting:

Sleeps 2 seconds between requests to be kind to the server

Robots.txt Compliance:

Scraper checks OpenLibrary’s rules before proceeding

## 🛡️ Error Handling

HTTP errors (timeouts, bad responses) are caught and logged

Missing elements in the DOM are safely handled

File read/write operations are wrapped in try-except blocks
