from models.library import Library
import system.interface_functions as sif

library1 = Library("Library")
library1.register("Bono", 1990, "bono@", "0000-AA", True)
library1.add_book("Book1", 1987, "SmartOne")
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
                            user_input = input("\nWelcome member, select a number from the list below:\n1) Browsing books\n2) Add new book\n3) Borrow book\n4) Unborrow book\n5) Profile\n6) Logout\n")
                            match user_input:
                                case '1':
                                    sif.list_books_interface(library1)
                                case '2':
                                    sif.add_book(library1)
                                case '3':
                                    sif.borrow_book(library1, user_input_ID)
                                case '4':
                                    sif.unborrow_book(library1, user_input_ID)
                                case '5':
                                    sif.profile(library1, user_input_ID)
                                case '6':
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



