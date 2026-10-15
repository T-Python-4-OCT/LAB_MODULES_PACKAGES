
def add_book(library, title, author, isbn):
    """Add a new book to the library."""
    if isbn in library:
        print("This ISBN already exists.")
    else:
        book = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "available": True
        }
        library[isbn] = book


def remove_book(library, isbn):
    """Remove a book from the library."""
    if isbn in library:
        del library[isbn]
    else:
        print("Book not found.")


def check_out_book(library, isbn):
    """Check out an available book."""
    if isbn not in library:
        print("Book not found.")
    elif library[isbn]["available"] == False:
        print("Book is already checked out.")
    else:
        library[isbn]["available"] = False


def return_book(library, isbn):
    """Return a book to the library."""
    if isbn not in library:
        print("Book not found.")
    else:
        library[isbn]["available"] = True


def display_books(library):
    """Display all books in the library."""
    for isbn in library:
        book = library[isbn]

        if book["available"] == True:
            status = "Available"
        else:
            status = "Checked Out"

        print(book["title"] + " by " + book["author"]
              + " (ISBN: " + book["isbn"] + ") - " + status)
