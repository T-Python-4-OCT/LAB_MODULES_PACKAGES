import dateOP 

from library import librarian


dateOP.current_date()

print("======"*20)


library = {}

# Add books
librarian.add_book(
    library,
    "The Catcher in the Rye",
    "J.D. Salinger",
    "9780316769174"
)

librarian.add_book(
    library,
    "To Kill a Mockingbird",
    "Harper Lee",
    "9780446310789"
)

librarian.add_book(
    library,
    "1984",
    "George Orwell",
    "9780451524935"
)

# Display all books
librarian.display_books(library)

print("\n--------------------\n")

# Check out a book
librarian.check_out_book(library, "9780316769174")
librarian.display_books(library)

print("\n--------------------\n")

# Return the book
librarian.return_book(library, "9780316769174")
librarian.display_books(library)

print("\n--------------------\n")

# Remove a book
librarian.remove_book(library, "9780451524935")
librarian.display_books(library)

