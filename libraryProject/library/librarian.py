library = {}


def add_book(library, title, author, isbn):
    if isbn in library:
        print("Book already exists.")
    else:
        library[isbn] = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "available": True
        }
        print("Book added successfully.")
        
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
        print("Book already checked out.")
    else:
        library[isbn]["available"] = False
        print("Book checked out successfully.")

def return_book(library, isbn):
    if isbn not in library:
        print("Book not found.")
    elif library[isbn]["available"]:
        print("Book is already available.")
    else:
        library[isbn]["available"] = True
        print("Book returned successfully.")

def display_books(library):
    if not library:
        print("Library is empty.")
        return

    for book in library.values():
        if book["available"]:
            status = "Available"
        else:
            status = "Checked out"

        print(
            f'{book["title"]} by {book["author"]} '
            f'(ISBN: {book["isbn"]}) - {status}'
        )
