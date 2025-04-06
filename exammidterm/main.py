from exammidterm.book import BookCollection
from exammidterm.scraper import OpenLibraryScraper

if __name__ == '__main__':
    scraper = OpenLibraryScraper()
    person = 'JDCarrr99/lists/OL207808L/New_Books'  # might want to change if its unavailable
    books = scraper.parse_book_info_from_people(person, 100, 5)

    print(f"Found {books.size()} books under person '{person}':")
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

    authors_with_multiple_books = books.get_authors_with_more_than_or_equal_to_x_books(3)
    print("Authors with 3 or more books:")

    for author, count in authors_with_multiple_books.items():
        print(f"{author}: {count}")
