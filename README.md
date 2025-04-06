# 📚 OpenLibrary Book Scraper

This Python project is a web scraper built to collect book data from [OpenLibrary.org](https://openlibrary.org). It fetches and parses content with Python, respecting Terms of Service & robots.txt rules, rate limits requests, and book information using BeautifulSoup.

---

## 🧠 What it does

- Scrapes books from a specific users' page on OpenLibrary (like science fiction, art, etc.)
- Collects details such as title, author, book URL, and cover image
- Saves the data in **JSON** and **CSV** formats
- Provides easy methods to:
  - Filter books by keywords in the title
  - Get all unique authors
- Handles errors gracefully (e.g. missing data, connection issues)
- Follows proper object-oriented design (OOP principles)

---

## 🛠️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/openlibrary-scraper.git
cd openlibrary-scraper


python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

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
