import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin
import re

from exammidterm.book import BookCollection, Book


class OpenLibraryScraper:
    BASE_URL = 'https://openlibrary.org/'
    HEADERS = {
        'User-Agent': 'OpenLibraryScraperBot/1.0 tesigo@gmail.com',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    RATE_LIMIT_SECONDS = 2

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)

    def is_allowed_by_robots(self, path):
        robots_url = urljoin(self.BASE_URL, 'robots.txt')
        try:
            response = self.session.get(robots_url)
            response.raise_for_status()
            disallowed_paths = re.findall(r'Disallow: (.+)', response.text)
            for disallowed in disallowed_paths:
                if path.startswith(disallowed):
                    print(f"Path {path} is disallowed by robots.txt")
                    return False
            return True
        except requests.RequestException as e:
            print(f"Error fetching robots.txt: {e}")
            return False

    def fetch_page(self, path):
        if not self.is_allowed_by_robots(path):
            return None
        full_url = urljoin(self.BASE_URL, path)
        try:
            response = self.session.get(full_url)
            response.raise_for_status()
            print(f"Fetched {full_url}")
            time.sleep(self.RATE_LIMIT_SECONDS)
            return response.text
        except requests.RequestException as e:
            print(f"Request failed for {full_url}: {e}")
            return None

    def parse_book_info_from_people(self, people, min_books_to_scrape=50, max_pages=5):
        page_num = 1

        book_collection = BookCollection()
        while book_collection.size() < min_books_to_scrape and page_num <= max_pages:
            path = f"/people/{people}?page={page_num}"
            print(f"Fetching page {page_num}: {path}")

            html = self.fetch_page(path)
            if html is None:
                print(f"Failed to fetch page {page_num} at {path}")
                return book_collection

            soup = BeautifulSoup(html, 'html.parser')

            print(f"Page {page_num} title: {soup.title.text if soup.title else 'No title'}")

            book_items = soup.select('.searchResultItem') or soup.select('.book-item') or soup.select('.listResults li')
            print(f"Found {len(book_items)} potential book items on page {page_num}")

            if not book_items:
                book_items = soup.select('li[itemtype*="Book"]') or soup.select('div[itemtype*="Book"]')
                print(f"Found {len(book_items)} items with alternative selectors on page {page_num}")

            if not book_items:
                print(f"No more books found on page {page_num}, ending pagination")
                break

            page_books = 0

            for book_item in book_items:
                try:
                    title_tag = (book_item.select_one('h3.booktitle') or
                                 book_item.select_one('.resultTitle') or
                                 book_item.select_one('h3 a') or
                                 book_item.select_one('h4 a'))
                    title = title_tag.get_text(strip=True) if title_tag else 'No title found'

                    link_tag = book_item.select_one('a[href*="/works/"]') or book_item.select_one('a')
                    link = urljoin(self.BASE_URL,
                                   link_tag['href']) if link_tag and 'href' in link_tag.attrs else 'No link found'

                    author_tag = (book_item.select_one('span.bookauthor') or
                                  book_item.select_one('.authorName') or
                                  book_item.select_one('.author'))
                    author = author_tag.get_text(strip=True) if author_tag else 'No author found'

                    cover_img_tag = book_item.select_one('img.cover') or book_item.select_one('img')
                    cover_img_url = cover_img_tag[
                        'src'] if cover_img_tag and 'src' in cover_img_tag.attrs else 'No cover image found'

                    book = Book(title, author[2:], link, cover_img_url)
                    book_collection.add_book(book)

                    page_books += 1

                except Exception as e:
                    print(f"Error parsing book item on page {page_num}: {e}")
                    print(f"Item HTML: {book_item.prettify()[:200]}...")

            print(f"Scraped {page_books} books from page {page_num}")

            next_page_link = soup.select_one('a.next') or soup.select_one('a[rel="next"]') or soup.select_one(
                '.pagination a:contains("Next")')

            if not next_page_link:
                break

            page_num += 1

        print(f"Pagination complete. Scraped a total of {book_collection.size()} books across {page_num} pages")
        return book_collection
