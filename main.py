import dateOP

from library import librarian

my_library={}
dateOP.date_time()

print("_"*50)
librarian.add_book(
    my_library,
    "The Catcher in the Rye",
    "J.D. Salinger",
    "9780316769174"
)

librarian.add_book(
    my_library,
    "To Kill a Mockingbird",
    "Harper Lee",
    "9780446310789"
)

librarian.add_book(
    my_library,
    "1984",
    "George Orwell",
    "9780451524935"
)


print("\n--- All Books ---")
librarian.display_books(my_library)


print("\n--- Check Out a Book ---")
librarian.check_out_book(my_library, "9780316769174")
librarian.display_books(my_library)


print("\n--- Return a Book ---")
librarian.return_book(my_library, "9780316769174")
librarian.display_books(my_library)


print("\n--- Remove a Book ---")
librarian.remove_book(my_library, "9780451524935")
librarian.display_books(my_library)
