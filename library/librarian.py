def add_book(library):
  title = input("Enter book title: ")
  author = input("Enter author name: ")
  isbn = input("Enter ISBN: ")

  if isbn in library:
    print(f"Book with ISBN {isbn} already exists in the library.")
  else:
    library[isbn] = {
        "title": title,
        "author": author,
        "available": True,
    }
    print(f"Book '{title}' added successfully.")


def remove_book(library):
  isbn = input("Enter ISBN of the book to remove: ")
  if isbn in library:
    del library[isbn]
    print(f"Book with ISBN {isbn} removed successfully.")
  else:
    print(f"Book with ISBN {isbn} not found in the library.")


def check_out_book(library):
  isbn = input("Enter ISBN of the book to check out: ")
  if isbn in library:
    if library[isbn]["available"]:
      library[isbn]["available"] = False
      print(f"Book '{library[isbn]['title']}' checked out successfully.")
    else:
      print(f"Book '{library[isbn]['title']}' is already checked out.")
  else:
    print(f"Book with ISBN {isbn} not found in the library.")


def return_book(library):
  isbn = input("Enter ISBN of the book to return: ")
  if isbn in library:
    library[isbn]["available"] = True
    print(f"Book '{library[isbn]['title']}' returned successfully.")
  else:
    print(f"Book with ISBN {isbn} not found in the library.")


def display_books(library):
  print("\n--- Library Books ---")
  if not library:
    print("The library is empty.")
  else:
    for isbn, info in library.items():
      status = "Available" if info["available"] else "Checked Out"
      print(f"{info['title']} by {info['author']} (ISBN: {isbn}) - {status}")
  print("---------------------\n")