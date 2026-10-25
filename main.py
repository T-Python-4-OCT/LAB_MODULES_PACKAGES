import dateOP
from library import librarian


def main():
    dateOP.print_current_date()
    print()

    library = {}

    librarian.add_book(library, "The Catcher in the Rye", "J.D. Salinger", "9780316769174")
    librarian.add_book(library, "To Kill a Mockingbird", "Harper Lee", "9780446310789")
    librarian.add_book(library, "1984", "George Orwell", "9780451524935")

    # Add and remove an extra book so the display matches the sample.
    librarian.add_book(library, "Pride and Prejudice", "Jane Austen", "9780141439518")
    librarian.remove_book(library, "9780141439518")
    librarian.display_books(library)
    print()

    librarian.check_out_book(library, "9780316769174")
    librarian.display_books(library)
    print()

    librarian.return_book(library, "9780316769174")
    librarian.display_books(library)


if __name__ == "__main__":
    main()
