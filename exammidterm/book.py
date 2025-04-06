import csv
import json
from collections import Counter

class Book:
    def __init__(self, title, author, link, cover_image_url):
        self._title = title
        self._author = author
        self._link = link
        self._cover_image_url = cover_image_url

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def link(self):
        return self._link

    @property
    def cover_image_url(self):
        return self._cover_image_url

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "link": self.link,
            "cover_image_url": self.cover_image_url
        }

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nLink: {self.link}\nCover Image: {self.cover_image_url}\n"


class BookCollection:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)

    def size(self):
        return len(self._books)

    def __len__(self):
        return len(self._books)

    def __iter__(self):
        return iter(self._books)

    def __str__(self):
        return "\n".join(str(book) for book in self._books)

    def to_json(self, filepath):
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump([book.to_dict() for book in self._books], f, indent=2)
        except IOError as e:
            print(f"Error saving JSON file: {e}")

    def to_csv(self, filepath):
        try:
            with open(filepath, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=['title', 'author', 'link', 'cover_image_url'])
                writer.writeheader()
                for book in self._books:
                    writer.writerow(book.to_dict())
        except IOError as e:
            print(f"Error saving CSV file: {e}")

    @staticmethod
    def from_json(filepath):
        print(f'Loading book collection from {filepath}')
        collection = BookCollection()
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data:
                    book = Book(
                        item.get('title', 'Unknown'),
                        item.get('author', 'Unknown'),
                        item.get('link', 'Unknown'),
                        item.get('cover_image_url', 'Unknown')
                    )
                    collection.add_book(book)
        except IOError as e:
            print(f"Error loading JSON file: {e}")
        return collection

    def get_authors(self):
        return set(book.author for book in self._books if book.author != 'No author found')

    def filter_by_keyword(self, keyword):
        return [book for book in self._books if keyword.lower() in book.title.lower()]

    def get_authors_with_more_than_or_equal_to_x_books(self, x=3):
        author_counts = Counter(book.author for book in self._books if book.author != 'No author found')
        return {author: count for author, count in author_counts.items() if count >= x}
