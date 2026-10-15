import dateOP


dateOP.print_current_date()

print()
print()

def add_book(library, title, author, isbn):
    if isbn in library:
        print(f"A book with ISBN {isbn} already exists.")
        return

    library[isbn] = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True,
    }


def remove_book(library, isbn):
    if isbn not in library:
        print(f"No book with ISBN {isbn} was found.")
        return

    del library[isbn]


def check_out_book(library, isbn):
    if isbn not in library:
        print(f"No book with ISBN {isbn} was found.")
        return

    if not library[isbn]["available"]:
        print(f"The book '{library[isbn]['title']}' is already checked out.")
        return

    library[isbn]["available"] = False


def return_book(library, isbn):
    if isbn not in library:
        print(f"No book with ISBN {isbn} was found.")
        return

    library[isbn]["available"] = True


def display_books(library):
    for book in library.values():
        status = "Available" if book["available"] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")


my_library = {}

add_book(my_library, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
add_book(my_library, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
add_book(my_library, "1984", "George Orwell", "9780451524935")

add_book(my_library, "Brave New World", "Aldous Huxley", "9780060850524")
remove_book(my_library, "9780060850524")

display_books(my_library)
print()

check_out_book(my_library, "9780316769174")
display_books(my_library)
print()

return_book(my_library, "9780316769174")
display_books(my_library)

#MoammedAlnsafi