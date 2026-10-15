def add_book(library, title, author, isbn):
    if isbn in library:
        print("Book already exists.")
        return

    library[isbn] = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True
    }


def remove_book(library, isbn):
    if isbn not in library:
        print("Book not found")
        return

    del library[isbn]
    print("Book removed")


def check_out_book(library, isbn):
    if isbn not in library:
        print("Book not found")
        return

    if not library[isbn]["available"]:
        print("Book not available")
        return

    library[isbn]["available"] = False
    print("Book checked out")


def return_book(library, isbn):
    if isbn not in library:
        print("Book not found")
        return

    library[isbn]["available"] = True
    print("Book returnwd")


def display_books(library):
    for isbn, book in library.items():
        status = "available" if book["available"] else "checked Out"
        print(
            f'{book["title"]} by {book["author"]} '
            f'(ISBN: {isbn}) - {status}'
        )