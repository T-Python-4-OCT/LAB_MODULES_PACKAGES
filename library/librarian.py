def add_book(library, title, author, isbn):
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
    if isbn not in library:
        print(f"No book with ISBN {isbn} was found in the library.")
        return
    del library[isbn]


def check_out_book(library, isbn):
    if isbn not in library:
        print(f"No book with ISBN {isbn} was found in the library.")
    elif not library[isbn]["available"]:
        print(f"'{library[isbn]['title']}' is already checked out.")
    else:
        library[isbn]["available"] = False


def return_book(library, isbn):
    if isbn not in library:
        print(f"No book with ISBN {isbn} was found in the library.")
    else:
        library[isbn]["available"] = True


def display_books(library):
    for book in library.values():
        status = "Available" if book["available"] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")