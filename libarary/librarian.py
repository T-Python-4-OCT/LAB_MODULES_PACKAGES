library =[]

def add_book(library, title, author, isbn):
    # library = str(input("enter the libarary name:"))
    # title = str(input("enter the title of the book:"))
    # author = str(input("enter the author name:"))
    # isbn = str (input("enter the book isbn:"))
    new_book ={
        "library" : library,
        "title":title,
        "author":author
        ,"isbn":isbn,
        "available":True

    }

    library.append(new_book)
    print (f"{title} add successfully")
def display_books (library):
    for num, book in enumerate (library,start=1):
        status = "Available" if book["available"] else "checked out"

        print(f"{num}.{book["title"]}by {book["author"]} (isbn: {book["isbn"]}) - {status}")


def remove_book(library,isbn):
    for  book in library :
        if book["isbn"] == isbn:
            (library.remove(book))
            print(f"Book with ISBN {isbn} removed successfully.")
            return


def check_out_book(library, isbn):
  for book in library:
    if book["isbn"] == isbn:
      if book["available"]:  
        book["available"] = False
        print(f"Book '{book['title']}' has been checked out.")
      else:
        print(f"Book '{book['title']}' is already checked out.")
      return  

  print(f"Book with ISBN {isbn} not found.")
            
def return_book (library,isbn):
   for book in library:
      if book["isbn"]==isbn:
         
        if book["available"] ==False:
          book["available"]=True
          print(f"Book '{book['title']}' has been returned.")
          return
   print(f"Book with ISBN {isbn} not found.")





            