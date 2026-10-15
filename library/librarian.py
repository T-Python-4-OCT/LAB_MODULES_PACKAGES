def add_book(library, title, author, isbn):
    if isbn in library:
        print("Book already exists")
    else:
        library[isbn] = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "available": True
        }


def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
    else:
        print("Book not found")


def check_out_book(library, isbn):
    if isbn not in library:
        print("Book not found")
    elif library[isbn]["available"] == False:
        print("Book is not available")
    else:
        library[isbn]["available"] = False


def return_book(library, isbn):
    if isbn in library:
        library[isbn]["available"] = True
    else:
        print("Book not found")


def display_books(library):
    for book in library.values():
        if book["available"]:
            status = "Available"
        else:
            status = "Checked Out"

        print(
            f'{book["title"]} by {book["author"]} '
            f'(ISBN: {book["isbn"]}) - {status}'
        )