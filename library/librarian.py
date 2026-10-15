def add_book(library, title, author, isbn):
    if isbn in library:
        print("This book already exists")
    else:
        library[isbn] = {
            'title': title,
            'author': author,
            'isbn': isbn,
            'available': True
        }

def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
    else:
        print("Sorry, this book does not exist.")
def check_out_book(library, isbn):
    if isbn not in library:
        print("Sorry, not found.")
    elif library[isbn]['available'] == False:
        print("The book is not available.")
    else:
        library[isbn]['available'] = False

def return_book(library, isbn):
    if isbn not in library:
        print("Sorry, not found.")
    else:
        library[isbn]['available'] = True

def display_books(library):
    for isbn, book in library.items():
        if book['available'] == True:
            status = "Available"
        else:
            status = "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {isbn}) - {status}")