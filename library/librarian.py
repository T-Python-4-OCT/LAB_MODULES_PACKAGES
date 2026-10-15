# library/librarian.py

def add_book(library, title, author, isbn):
    if isbn in library:
        print(f"Book with ISBN {isbn} already exists.")
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
        print(f"Book with ISBN {isbn} does not exist in the library.")

def check_out_book(library, isbn):
    if isbn not in library:
        print(f"Book with ISBN {isbn} does not exist.")
    elif not library[isbn]["available"]:
        print(f"Book is already checked out.")
    else:
        library[isbn]["available"] = False

def return_book(library, isbn):
    if isbn not in library:
        print(f"Book with ISBN {isbn} does not exist.")
    else:
        library[isbn]["available"] = True

def display_books(library):
    for book in library.values():
        status = "Available" if book["available"] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")
    print()  