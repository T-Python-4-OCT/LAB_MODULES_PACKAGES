
from dateOP import get_today_date

print("-" * 60)
print("lab_1:")
get_today_date()
print("-" * 60)

print("______Welcome to the Library Management System!_______________________")
from library import librarian

def main():
    my_library = {}

    librarian.add_book(my_library, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
    librarian.add_book(my_library, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
    librarian.add_book(my_library, "1984", "George Orwell", "9780451524935")

    librarian.display_books(my_library)

    librarian.check_out_book(my_library, "9780316769174")

    librarian.display_books(my_library)

    librarian.return_book(my_library, "9780316769174")

    librarian.display_books(my_library)

if __name__ == "__main__":
    main()