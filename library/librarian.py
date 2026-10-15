def add_book(library, title, author, isbn):
    if isbn in library:
        print("This book already exists.")
    else:
        library[isbn] = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "available": True
        }
        print(f"Book added: {title}")




def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
        print("Book removed successfully.")
    else:
        print("Book not found.")


def check_out_book(library, isbn):
    if isbn not in library:
        print("Book not found.")
    elif not library[isbn]["available"]:
        print("Book is already checked out.")
    else:
        library[isbn]["available"] = False
        print("Book checked out successfully.")


def return_book(library, isbn):
    if isbn not in library:
        print("Book not found.")
    else:
        library[isbn]["available"] = True
        print("Book returned successfully.")


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