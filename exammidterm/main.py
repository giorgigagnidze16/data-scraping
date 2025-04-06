from exammidterm.book import BookCollection
from exammidterm.midterm import OpenLibraryScraper

if __name__ == '__main__':
    scraper = OpenLibraryScraper()
    person = 'JDCarrr99/lists/OL207808L/New_Books'
    books = scraper.parse_book_info_from_people(person, 100)

    print(f"Found {len(books)} books under subject '{person}':")
    print(books)

    # write to files
    books.to_csv("books.csv")
    books.to_json("books.json")

    # load and analyze
    loaded_books = BookCollection.from_json('books.json')

    print("\nUnique authors:")
    print(loaded_books.get_authors())

    print("\nBooks with 'war' in title:")
    filtered = loaded_books.filter_by_keyword('war')
    for book in filtered:
        print(book)
