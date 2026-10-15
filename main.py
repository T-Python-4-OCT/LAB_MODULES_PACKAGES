print("MY MAIN FILE IS RUNNING")
from dateOP import current_date
from library import librarian


current_date()
print("DATE TEST COMPLETE")

print("--" * 15)


library = {}


librarian.add_book(library, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
librarian.add_book(library, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
librarian.add_book(library, "1984", "George Orwell", "9780451524935")


librarian.display_books(library)
print()


librarian.check_out_book(library, "9780316769174")
librarian.display_books(library)
print()

librarian.remove_book(library, "9780451524935")
librarian.display_books(library)
print()


librarian.return_book(library, "9780316769174")
librarian.display_books(library)