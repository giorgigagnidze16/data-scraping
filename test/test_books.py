import unittest
from exammidterm.book import Book, BookCollection


class TestBookCollection(unittest.TestCase):

    def setUp(self):
        self.book1 = Book("Title1", "Author1", "https://example.com/book1", "https://example.com/img1.jpg")
        self.book2 = Book("Title2", "Author1", "https://example.com/book2", "https://example.com/img2.jpg")
        self.book3 = Book("War Book", "Author2", "https://example.com/book3", "https://example.com/img3.jpg")
        self.collection = BookCollection()
        self.collection.add_book(self.book1)
        self.collection.add_book(self.book2)
        self.collection.add_book(self.book3)

    def test_size(self):
        self.assertEqual(self.collection.size(), 3)

    def test_get_authors(self):
        authors = self.collection.get_authors()
        self.assertIn("Author1", authors)
        self.assertIn("Author2", authors)

    def test_filter_by_keyword(self):
        filtered = self.collection.filter_by_keyword("war")
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].title, "War Book")

    def test_authors_with_multiple_books(self):
        result = self.collection.get_authors_with_more_than_or_equal_to_x_books(2)
        self.assertIn("Author1", result)
        self.assertEqual(result["Author1"], 2)
