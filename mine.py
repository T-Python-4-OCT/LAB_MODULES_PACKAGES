import dateOP

from library.librarian import library,return_book,remove_book,check_out_book,add_book,display_books

print(dateOP.prh())

add_book(library, "top for top", "mohammed", "2222")
check_out_book(library,"2222")
remove_book(library,"123456")
display_books(library)
