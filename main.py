from library import librarian

library_catalog = {}

print("--- Library Management System ---")

while True:
  print("\nChoose an option:")
  print("1. Add a book")
  print("2. Remove a book")
  print("3. Check out a book")
  print("4. Return a book")
  print("5. Display all books")
  print("6. Exit")

  choice = input("Enter your choice (1-6): ")

  if choice == "1":
    librarian.add_book(library_catalog)
  elif choice == "2":
    librarian.remove_book(library_catalog)
  elif choice == "3":
    librarian.check_out_book(library_catalog)
  elif choice == "4":
    librarian.return_book(library_catalog)
  elif choice == "5":
    librarian.display_books(library_catalog)
  elif choice == "6":
    print("Exiting program. Goodbye!")
    break
  else:
    print("Invalid choice, please try again.")