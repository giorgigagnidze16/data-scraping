# NOTE: I'M SCRAPING DATA FROM USERS' (JDCarrr99/lists/OL207808L/New_Books) PERSONAL PAGES SINCE WHEN I WAS TRYING TO SCRAP DATA PER SUBJECT (SCIENCE FICTION, etc..) SERVICE WAS ALWAYS UNAVAILABLE RETURNING TIMEOUTS, THEREFORE THIS WAS THE WAY

# 📄 Web Scraping Project Report: OpenLibrary.org

## 1. Website Chosen and Why

For this scraping project, I chose [OpenLibrary.org](https://openlibrary.org) — digital library that aims to create a
web page for every book ever published. It organizes book data into multiple formats, per-subject, per-user, etc making
it suitable for structured scraping of key information such as titles, authors, cover images, and book detail links.

The main reason I selected this site is that **OpenLibrary provides a well-defined and accessible `robots.txt` file**.
Legal and compliant scraping is important, and many websites either block bots entirely or don't expose scraping
policies. OpenLibrary explicitly states which paths are restricted, allowing the scraper to operate within permitted
bounds.

## 2. Implementation Challenges and Solutions

### a. Robots.txt Compliance

A key challenge was ensuring the scraper respected OpenLibrary's `robots.txt` file. I implemented a function to fetch
and parse this file using regex to extract `Disallow` rules. Before accessing any path, the scraper checks it against
this list and skips it if it's disallowed.

### b. Inconsistent HTML Structures

OpenLibrary’s HTML structure for books is not entirely consistent across different pages. Some entries lack elements
like author names or cover images, which could cause the scraper to crash.

To solve this I used several BS4 techniques:

- `select_one()` with CSS selectors
- Navigating nested tags
- Extracting text, attributes, and links
- Error handling for each field to ensure resilience

This allowed the scraper to continue extracting data even when some fields were missing.

### c. Rate Limiting and HTTP Error Handling

To prevent overwhelming and stressing the website or getting IP-blocked, I implemented **rate limiting** by adding a
2-second delay between requests. Additionally, all HTTP operations are wrapped in `try-except` blocks to handle network
issues, timeouts, and HTTP status errors gracefully.

## 3. Analysis of Collected Data

The data collected includes the following attributes for each book:

- `title`: The book's title
- `author`: The name of the author
- `link`: URL to the book's page
- `cover_image_url`: URL of the cover image

This data is saved in both **CSV** and **JSON** formats to support various downstream use cases.

### Post-Processing & Analysis

Analytical data implemented:

- **Unique author listing**: Extracts and lists all unique authors from the dataset.
- **Paginate Scraping**: Paginate through the pages, to scrap as many books as possible.
- **Keyword filtering**: Filters books whose titles contain a given keyword (e.g., "war").
- **Author Statistics**: Find authors who have written >= x books in total from the scraped list.
- **Statistics Visualization**: Visualize the above statistics data using matplotlib.

Project also contains unit testing for verification purposes.

Example usage:

```bash
Books with 'war' in title:
- War of the Worlds
- Galactic War Chronicles
```

# Potential Improvements and Extensions

While the scraper works well for its current scope, several improvements could enhance its capabilities:

Command-line Arguments: Supporting dynamic user input via CLI would improve flexibility instead of hard coded users now.

Database Integration: Using SQLite or MongoDB for persistent storage and advanced querying & analysis for machine
learning in the future to predict and learn users' fav genres'.

Scraping Book Details: Extracting additional data such as descriptions, publication dates, or ratings by visiting
individual book pages.