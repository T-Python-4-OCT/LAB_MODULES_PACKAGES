# Lab Modules and Packages

def add_book(library, title, author, isbn):

    if isbn in library:
        print(f"A book with ISBN is {isbn} already exists.")
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
        print(f"No book with ISBN {isbn} was found.")


def check_out_book(library, isbn):
    if isbn not in library:
        print(f"No book with ISBN {isbn} was found.")
    elif library[isbn]["available"] == False:
        print(f"The book with ISBN {isbn} is already checked out.")
    else:
        library[isbn]["available"] = False


def return_book(library, isbn):
    if isbn in library:
        library[isbn]["available"] = True
    else:
        print(f"No book with ISBN {isbn} was found.")

def display_books(library):
    for isbn in library:
        book = library[isbn]

        if book["available"]:
            status = "Available"
        else:
            status = "Checked Out"

        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")
    print()