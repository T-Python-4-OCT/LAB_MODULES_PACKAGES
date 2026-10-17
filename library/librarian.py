#


def add_book(library, title:str, author:str, isbn:str):
    if isbn in library:
        print("book already exists!")
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
        print("Book removed successfully")
    else:
        print("Book not found in the library")


def check_out_book(library, isbn):
    if isbn not in library:
        print("Book not found in the library.")
    elif not library[isbn]["available"]:
        print("Book is already checked out.")
    else:
        library[isbn]["available"] = False
        print("Book checked out successfully.")



def return_book(library, isbn):
    if isbn not in library:
        print("Book not found in the library.")
    else:
        library[isbn]["available"] = True
        print("Book returned successfully.")

def display_books(library):
    if not library:
        print("The library is empty.")
        return

    for book in library.values():
        status = "Available" if book["available"] else "Checked Out"

        print(
            f'{book["title"]} by {book["author"]} '
            f'(ISBN: {book["isbn"]}) - {status}'
        )






