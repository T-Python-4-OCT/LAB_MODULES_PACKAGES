
from library import librarian

librarian.add_book(
    librarian.library,
    "The Catcher in the Rye",
    "J.D. Salinger",
    "9780316769174"
)
librarian.add_book(
    librarian.library,
    "To Kill a Mockingbird",
    "Harper Lee",
    "9780446310789"
)
librarian.add_book(
    librarian.library,
    "1984",
    "George Orwell",
    "9780451524935"
)
print("\nAll Books:")
librarian.display_books(librarian.library)
print("\nAfter Checkout:")
librarian.check_out_book(
    librarian.library,
    "9780316769174"
)
librarian.display_books(librarian.library)
print("\nAfter Return:")
librarian.return_book(
    librarian.library,
    "9780316769174"
)
librarian.display_books(librarian.library)
print("\nAfter Removing:")
librarian.remove_book(
    librarian.library,
    "9780451524935"
)
librarian.display_books(librarian.library)
