import dataOP

dataOP.print_date()

from library import librarian
 


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

print()

# Check out a book
librarian.check_out_book(library, "9780316769174")

# Display books after checkout
librarian.display_books(library)

print()

# Return the book
librarian.return_book(library, "9780316769174")

# Display books after returning
librarian.display_books(library)