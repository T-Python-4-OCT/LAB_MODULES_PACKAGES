
def add_book(library:dict,title:str,author:str,isbn:str):
    if isbn in library:
        print("This Book already exists.")
    else:
        library[isbn] = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "available":True
        }
        print(f"Book '{title}' added successfully.")

def remove_book(library:dict,isbn:str):
    if isbn in library:
        del library[isbn]
        print("Delete successfully")
    else:
        print("Book not found")

def check_out_book(library:dict,isbn:str):
    if isbn not in library:
        print("Book not found.")
    elif not library[isbn]["available"]:
        print("This book is already checked out.")
    else:
        library[isbn]["available"] = False
        print("Book checked out successfully.")

def return_book(library:dict, isbn:str):
    if isbn not in library:
        print("Book not found.")
    else:
        library[isbn]["available"] = True
        print("Book returned successfully.")

def display_books(library:dict):
    if not library:
        print("The library is empty.")
        return

    for book in library.values():
        if book["available"]:
            status = "Available"
        else:
            status = "Checked Out"

        print(
            f'{book["title"]} by {book["author"]} '
            f'(ISBN: {book["isbn"]}) - {status}'
        )
