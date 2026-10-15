

from library import librarian

my_library = {}

librarian.add_book(my_library, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
librarian.add_book(my_library, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
librarian.add_book(my_library, "1984", "George Orwell", "9780451524935")
librarian.add_book(my_library, "Brave New World", "Aldous Huxley", "9780060850524")

librarian.remove_book(my_library, "9780060850524")

librarian.display_books(my_library)
print()

librarian.check_out_book(my_library, "9780316769174")
librarian.display_books(my_library)
print()

librarian.return_book(my_library, "9780316769174")
librarian.display_books(my_library)