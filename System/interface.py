from models.library import Library
import system.interface_functions as sif

library1 = Library("Library")
library1.register("Bono", 1990, "bono@", "0000-AA", True)
library1.add_book("Book1", 1987, "SmartOne")
print("\nWelcome to the Library")

def run():
    while True:
        user_input = input("\nWelcome Visitor, select a number from the list below:\n1) Browsing books\n2) Login as member\n3) Register as new member\n4) Search book via title\n5) Search book via date\n6) Search book via author\n7) Leave Library\n")
        match user_input:
            case '0':
                library1.list_members()
            case '1':
                sif.list_books_interface(library1)
            case '2':
                member_run()
            case '3':
                sif.register_interface(library1)
            case '4':
                sif.search_book_title_interface(library1)
            case '5':
                sif.search_book_date_interface(library1)
            case '6':
                sif.search_book_author_interface(library1)
            case '4':
                print("Thank you for visiting, have a nice day!")
                break
            case _ :
                print("Not recognizable input, please select a number from the list provided.")

def member_run():
    user_input_email = input("\nEnter member email: ")
    user_input_ID = input("\nEnter member ID:\n")
    user_input_access, member_name = sif.login_interface(library1, user_input_ID, user_input_email)
    while True:
        match user_input_access:
            case True:
                user_input = input(f"\nWelcome member {member_name}, select a number from the list below:\n1)  Browsing books\n2)  Login as librarian\n3)  Add new book\n4)  Borrow book\n5)  Unborrow book\n6)  Profile\n7)  Search book via title\n8)  Search book via date\n9)  Search book via author\n10) Logout\n")
                match user_input:
                    case '1':
                        sif.list_books_interface(library1)           
                    case '2':
                        librarian_run(user_input_ID)
                    case '3':
                        sif.add_book_interface(library1)
                    case '4':
                        sif.borrow_book_interface(library1, user_input_ID)
                    case '5':
                        sif.unborrow_book_interface(library1, user_input_ID)
                    case '6':
                        sif.profile_interface(library1, user_input_ID)
                    case '7':
                        sif.search_book_title_interface(library1)
                    case '8':
                        sif.search_book_date_interface(library1)
                    case '9':
                        sif.search_book_author_interface(library1)
                    case '10':
                        print("Logout successfully")
                        break
                    case _:
                        print("Not recognizable input, please select a number from the list provided.")
            case _:
                print("Wrong access ID")
                break

def librarian_run(user_input_ID):
    user_input_access_librarian, member_name = sif.login_librarian_interface(library1, user_input_ID)
    while True:
        match user_input_access_librarian:
            case True:
                user_input = input(f"\nWelcome Librarian {member_name}, select a number from the list below:\n1)  Browsing books\n2)  List members\n3)  Add new book\n4)  Borrow book\n5)  Unborrow book\n6)  Profile\n7)  Register new member\n8)  Delete member\n9)  Delete book\n10) Modify member data\n11) Save members to file\n12) Load member from file\n13) Save books to file\n14) Load books from file\n15) Search for member via email\n16) Search for member via ID\n17) Search book via title\n18) Search book via date\n19) Search book via author\n20) Logout\n")
                match user_input:
                    case '1':
                        sif.list_books_interface(library1)
                    case '2':
                        sif.list_members_interface(library1)
                    case '3':
                        sif.add_book_interface(library1)
                    case '4':
                        sif.borrow_book_interface(library1, user_input_ID)
                    case '5':
                        sif.unborrow_book_interface(library1, user_input_ID)
                    case '6':
                        sif.profile_interface(library1, user_input_ID)
                    case '7':
                        sif.register_interface(library1)
                    case '8':
                        sif.delete_member_interface(library1)
                    case '9':
                        sif.delete_book_interface(library1)
                    case '10':
                        sif.modify_member(library1)
                    case '11':
                        sif.save_members_to_file_interface(library1)
                    case '12':
                        sif.load_members_from_file_interface(library1)
                    case '13':
                        sif.save_books_to_file_interface(library1)
                    case '14':
                        sif.load_books_from_file_interface(library1)
                    case '15':
                        sif.search_member_email_interface(library1)
                    case '16':
                        sif.search_member_ID_interface(library1)
                    case '17':
                        sif.search_book_title_interface(library1)
                    case '18':
                        sif.search_book_date_interface(library1)
                    case '19':
                        sif.search_book_author_interface(library1)
                    case '20':
                        print("Logout successfully")
                        break
                    case _:
                        print("Not recognizable input, please select a number from the list provided.")
            case _:
                print("Wrong access")
                break
