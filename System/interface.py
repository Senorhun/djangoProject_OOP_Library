from models.library import Library
from models.book import book_list
from models.person import people_list
import system.interface_functions as sif

library1 = Library("Library", people_list, book_list)
library1.register("Bono", 1990, "bono@", "0000-AA", True)
print("\nWelcome to the Library")

def run():
    while True:
        user_input = input("\nWelcome Visitor, select a number from the list below:\n1) Browsing books\n2) Login as member\n3) Register as new member\n4) Leave Library\n")
        match user_input:
            case '0':
                library1.list_members()
            case '1':
                sif.list_books_interface(library1)
            case '2':
                user_input_email = input("\nEnter member email: ")
                user_input_ID = input("\nEnter member ID:\n")
                user_input_access = sif.login_interface(library1, user_input_ID, user_input_email)
                while True:
                    match user_input_access:
                        case True:
                            print("Successfull login")
                            user_input = input("\nWelcome member, select a number from the list below:\n1) Browsing books\n2) Add new book\n3) Borrow book\n4) Logout\n")
                            match user_input:
                                case '1':
                                    sif.list_books_interface(library1)
                                case '2':
                                    pass
                                case '3':
                                    pass
                                case '4':
                                    print("Logout successfully")
                                    break
                        case _:
                            print("Wrong access ID")
                            break
            case '3':
                sif.register_interface(library1)
            case '4':
                print("Thank you for visiting, have a nice day!")
                break
            case _ :
                print("Not recognizable input, please select a number from the list provided.")



