import dateOP

print("\n ----- Today's date ----- ")

dateOP.print_date()

print("\n ----- Library System ----- ")

from library import librarian


library = {}

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

print("\n ----- All Books ----- ")
librarian.display_books(library)

print("\n ----- Check Out a Book ----- ")
librarian.check_out_book(library, "9780316769174")

print("\n ----- Books After Checkout ----- ")
librarian.display_books(library)

print("\n ----- Return a Book ----- ")
librarian.return_book(library, "9780316769174")

print("\n ----- Books After Return ----- ")
librarian.display_books(library)

print("\n ----- Remove a Book ----- ")
librarian.remove_book(library, "9780451524935")

print("\n ----- Books After Removal ----- ")
librarian.display_books(library)