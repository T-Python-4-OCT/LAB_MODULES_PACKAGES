from dateOP import get_current_date
from library.librarian import add_book, remove_book, check_out_book, return_book, display_books

library = {}


while True:
    print("\n========================")
    print("       MAIN MENU")
    print("========================")
    print("1. Today date")
    print("2. Library program")
    print("3. End program")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("\nPlease enter a number only.")
        continue


    if choice == 1:
        current_date = get_current_date()

        print("\n------------------------")
        print(f"Current Date: {current_date}")
        print("------------------------")


    elif choice == 2:

        while True:
            print("\n========================")
            print("      LIBRARY MENU")
            print("========================")
            print("1. Add book")
            print("2. Remove book")
            print("3. Check out book")
            print("4. Return book")
            print("5. Display books")
            print("6. Back")

            try:
                sub_choice = int(input("Enter your choice: "))
            except ValueError:
                print("\nPlease enter a number only.")
                continue


            if sub_choice == 1:
                print("\n--- Add Book ---")

                title = input("Enter book title: ")
                author = input("Enter book author: ")
                isbn = input("Enter ISBN: ")

                add_book(library, title, author, isbn)


            elif sub_choice == 2:
                print("\n--- Remove Book ---")

                isbn = input("Enter ISBN: ")

                remove_book(library, isbn)


            elif sub_choice == 3:
                print("\n--- Check Out Book ---")

                isbn = input("Enter ISBN: ")

                check_out_book(library, isbn)


            elif sub_choice == 4:
                print("\n--- Return Book ---")

                isbn = input("Enter ISBN: ")

                return_book(library, isbn)


            elif sub_choice == 5:
                display_books(library)


            elif sub_choice == 6:
                break


            else:
                print("\nInvalid choice.")


    elif choice == 3:
        print("\nProgram ended.")
        break


    else:
        print("\nInvalid choice.")