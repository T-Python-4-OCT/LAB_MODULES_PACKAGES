def add_book(library, title, author, isbn):
    """Add a new book to the library, keyed by its ISBN."""
    if isbn in library:
        print(f"A book with ISBN {isbn} already exists in the library.")
        return
    library[isbn] = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True,
    }


def remove_book(library, isbn):
    """Remove the book with the given ISBN from the library."""
    if isbn not in library:
        print(f"No book with ISBN {isbn} was found in the library.")
        return
    del library[isbn]


def check_out_book(library, isbn):
    """Mark the book with the given ISBN as checked out."""
    if isbn not in library:
        print(f"No book with ISBN {isbn} was found in the library.")
        return
    if not library[isbn]["available"]:
        print(f"'{library[isbn]['title']}' is already checked out.")
        return
    library[isbn]["available"] = False


def return_book(library, isbn):
    """Mark the book with the given ISBN as available again."""
    if isbn not in library:
        print(f"No book with ISBN {isbn} was found in the library.")
        return
    library[isbn]["available"] = True


def display_books(library):
    """Print every book in the library with its availability status."""
    if not library:
        print("The library has no books.")
        return
    for book in library.values():
        status = "Available" if book["available"] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")
    print()
