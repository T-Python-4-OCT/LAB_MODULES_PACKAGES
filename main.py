# ⏰ Date Assignment
import dateOP
from library import librarian

dateOP.current_date()



# 📚 Library Assignment

my_library = {}

print("📚✨ MY LIBRARY SYSTEM ✨📚")
print("=" * 35)

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

print("\n -- Library Collection --📚")
librarian.display_books(my_library)

print("\n-- Borrow a Book --📕")
librarian.check_out_book(my_library, "9780316769174")
librarian.display_books(my_library)

print("\n-- Give Back the Book --📗")
librarian.return_book(my_library, "9780316769174")
librarian.display_books(my_library)

print("\n -- Delete a Book 🗑️--")
librarian.remove_book(my_library, "9780451524935")
librarian.display_books(my_library)

print("\n✨ Library operations finished!✨✅ ")