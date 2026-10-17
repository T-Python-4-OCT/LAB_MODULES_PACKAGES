def add_book(library, title, author, isbn):
    """Adds a new book to the library dictionary."""
    if isbn in library:
        print(f"Error: A book with ISBN {isbn} already exists in the library.")
    else:
     library[isbn] = {
            'title': title,
            'author': author,
            'isbn': isbn,
            'available': True
        }
     print(f"Success: '{title}' by {author} has been added.")


def remove_book(library, isbn):
    """Removes a book from the library using its ISBN."""
    if isbn in library:
        removed_title = library[isbn]['title']
        del library[isbn]
        print(f"Success: '{removed_title}' (ISBN: {isbn}) has been removed.")
    else:
        print(f"Error: Book with ISBN {isbn} does not exist in the library.")


def check_out_book(library, isbn):
    """Checks out a book by setting its availability to False."""
    if isbn not in library:
        print(f"Error: Book with ISBN {isbn} does not exist in the library.")
    elif not library[isbn]['available']:
        print(f"Error: '{library[isbn]['title']}' is currently not available (already checked out).")
    else:
        library[isbn]['available'] = False
        print(f"Success: '{library[isbn]['title']}' has been checked out.")


def return_book(library, isbn):
    """Returns a book by setting its availability to True."""
    if isbn not in library:
        print(f"Error: Book with ISBN {isbn} does not exist in the library.")
    else:
        library[isbn]['available'] = True
        print(f"Success: '{library[isbn]['title']}' has been returned and is now available.")


def display_books(library):
    """Displays all books currently in the library in a formatted way."""
    if not library:
        print("\nThe library is currently empty.")
        return

    print("\n" + "=" * 40)
    print("           LIBRARY INVENTORY           ")
    print("=" * 40)
    for isbn, book in library.items():
        status = "Available" if book['available'] else "Checked Out"
        print(f"Title:     {book['title']}")
        print(f"Author:    {book['author']}")
        print(f"ISBN:      {isbn}")
        print(f"Status:    {status}")
        print("-" * 40)