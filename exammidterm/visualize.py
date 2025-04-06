import matplotlib.pyplot as plt
from collections import Counter


def plot_authors_with_many_books(book_collection, threshold=3):
    author_counts = Counter(book.author for book in book_collection if book.author != 'No author found')
    filtered_authors = {author: count for author, count in author_counts.items() if count >= threshold}

    if not filtered_authors:
        print("No authors with enough books for visualization.")
        return

    plt.figure(figsize=(10, 6))
    plt.bar(filtered_authors.keys(), filtered_authors.values(), color='skyblue')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel("Author")
    plt.ylabel("Number of Books")
    plt.title(f"Authors with ≥{threshold} Books")
    plt.tight_layout()
    plt.show()


def plot_top_authors_pie(book_collection, top_n=10):
    author_counts = Counter(book.author for book in book_collection if book.author != 'No author found')
    top_authors = dict(author_counts.most_common(top_n))

    plt.figure(figsize=(8, 8))
    plt.pie(top_authors.values(), labels=top_authors.keys(), autopct='%1.1f%%', startangle=140)
    plt.title(f"Top {top_n} Authors by Book Count")
    plt.axis('equal')
    plt.show()


def plot_books_per_author_hist(book_collection):
    author_counts = Counter(book.author for book in book_collection if book.author != 'No author found')
    book_counts = list(author_counts.values())

    plt.figure(figsize=(8, 6))
    plt.hist(book_counts, bins=range(1, max(book_counts) + 2), color='green', edgecolor='black')
    plt.xlabel("Number of Books")
    plt.ylabel("Number of Authors")
    plt.title("Distribution of Books per Author")
    plt.tight_layout()
    plt.show()
