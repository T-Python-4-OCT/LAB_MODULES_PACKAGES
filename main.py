import dateOP



dateOP.print_date()

print("*-------------------------------------------------------------------------*")


from library import librarian

my_library = {}

# add books to the library
librarian.add_book(my_library, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
librarian.add_book(my_library, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
librarian.add_book(my_library, "1984", "George Orwell", "9780451524935")
librarian.add_book(my_library, "The Hobbit", "J.R.R. Tolkien", "9780547928227")

# remove a book from the library
librarian.remove_book(my_library, "9780547928227")

librarian.display_books(my_library)

# check out a book from the library
librarian.check_out_book(my_library, "9780316769174")
librarian.display_books(my_library)

# return the book to the library
librarian.return_book(my_library, "9780316769174")
librarian.display_books(my_library)