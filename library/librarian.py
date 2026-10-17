def add_book(library: dict, title: str, author: str, isbn: str) -> None:
    """Add a book to the library."""

    title = title.strip()
    author = author.strip()
    isbn = isbn.strip()

    if title == "":
        print("Title cannot be empty.")
        return

    if author == "":
        print("Author cannot be empty.")
        return

    if isbn == "":
        print("ISBN cannot be empty.")
        return

    if isbn in library:
        print(f"Book with the ISBN {isbn} already exists in the library.")
        return

    library[isbn] = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True
    }

    print(f"Book '{title}' added successfully.")


def remove_book(library: dict, isbn: str) -> None:
    """Remove a book from the library."""

    isbn = isbn.strip()

    if isbn == "":
        print("ISBN cannot be empty.")
        return

    if isbn not in library:
        print(f"Book with the ISBN {isbn} does not exist in the library.")
        return

    title = library[isbn]["title"]

    del library[isbn]

    print(f"Book '{title}' removed successfully.")


def check_out_book(library: dict, isbn: str) -> None:
    """Check out a book from the library."""

    isbn = isbn.strip()

    if isbn == "":
        print("ISBN cannot be empty.")
        return

    if isbn not in library:
        print(f"Book with the ISBN {isbn} does not exist in the library.")
        return

    if not library[isbn]["available"]:
        print(f"Book '{library[isbn]['title']}' is already checked out.")
        return

    library[isbn]["available"] = False

    print(f"Book '{library[isbn]['title']}' checked out successfully.")


def return_book(library: dict, isbn: str) -> None:
    """Return a book to the library."""

    isbn = isbn.strip()

    if isbn == "":
        print("ISBN cannot be empty.")
        return

    if isbn not in library:
        print(f"Book with the ISBN {isbn} does not exist in the library.")
        return

    if library[isbn]["available"]:
        print(f"Book '{library[isbn]['title']}' is already available.")
        return

    library[isbn]["available"] = True

    print(f"Book '{library[isbn]['title']}' returned successfully.")


def display_books(library: dict) -> None:
    """Display all books in the library."""

    if not library:
        print("\nThe library is empty.")
        return

    print("\n==============================================")
    print("               LIBRARY BOOKS")
    print("==============================================")

    for isbn, book in library.items():
        status = "Available" if book["available"] else "Checked Out"

        print(
            f"{book['title']} by {book['author']} (ISBN: {isbn}) - {status}")
        print("----------------------------------------------")