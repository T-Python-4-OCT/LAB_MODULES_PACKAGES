def add_book(library, title: str, author: str, isbn: str) :

    new_book = {
        "title" : title,
        "author" : author,
        "isbn" : isbn,
        "available" : True
    }

    if isbn in library :
        print('The Book is Already exist')
    else :
        library[isbn] = new_book


def remove_book(library, isbn:str) :
    if isbn in library :
        del library[isbn]
    else :
        print('The Book is Not Found in the Library')
       
def check_out_book(library, isbn: str) :
    if isbn not in library :
        print('The Book is Not Found in the Library')
    
    elif library[isbn]['available'] == False :
        print('The Book Already Booked')

    else :
        library[isbn]['available'] = False
        print('Book checked out successfully!')

def return_book(library, isbn) :
    if isbn not in library:
        print('The Book is Not Exist in the Library')
    
    elif library[isbn]['available'] == False :
        library[isbn]['available'] = True

    else :
        print('The Book is Already Available')

def display_books(library) :
    for isbn in library :
        book = library[isbn]

        status = "Available" if book['available'] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")
