library = {
"12345": {"title": "Python Basics","author": "Ahmed","ISBN": "12345","Available": True},
"123456": {"title": "Python Basics","author": "Ahmed","ISBN": "123456","Available": True}}


def add_book(library, title, author, isbn):
    if isbn in library:
        print("Book already exists!")
    else:
        library[isbn] = {
            "title": title,
            "author": author,
            "ISBN": isbn,
            "Available": True
            }
        print("Book added successfully!")


def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
        print("Book removed successfully!")
    else:
        print("Book not found!")


def check_out_book(library, isbn):
    if isbn not in library:
        print("Book not found!")
    elif library[isbn]["Available"] == False:
        print("Book is already checked out!")
    else:
        library[isbn]["Available"] = False
        print("Book checked out successfully!")


def return_book(library, isbn):
    if isbn not in library:
        print("Book not found!")
    elif library[isbn]["Available"] == True:
        print("Book is already available!")
    else:
        library[isbn]["Available"] = True
        print("Book returned successfully!")


def display_books(library):
    if not library:
        print("The library is empty!")
        return

    for isbn, book in library.items():
        if book["Available"]:
            status = "Available"
        else:
            status = "Checked Out"

        print(f"{book['title']} by {book['author']} "
              f"(ISBN: {isbn}) - {status}")