from models.library import Library
import system.interface_functions as sif

library1 = Library("Library")
library1.register("Bono", 1990, "bono@", "0000-AA", True)
library1.add_book("Book1", 1987, "SmartOne")
print("\nWelcome to the Library")

def librarian_interface():
    while True:
        user_input = input("\nSelect a number from the list below:\n1) List members\n2) Register new member\n3) Modify member data\n4) Delete member\n5) Save members to file\n6) Load members from file\n7) Search member via email\n8) Search member via ID\n9) Exit")
        match user_input: 
            case '1':
                sif.list_members_interface(library1) 
            case '2':
                sif.register_interface(library1)
            case '3':
                sif.modify_member(library1)
            case '4':
                sif.delete_member_interface(library1)
            case '5':
                sif.save_members_to_file_interface(library1)
            case '6':
                sif.load_members_from_file_interface(library1)
            case '7':
                sif.search_member_email_interface(library1)
            case '8':
                sif.search_member_ID_interface(library1)
            case '9':
                break
            

def books_run():
    while True:
        user_input = input("\nSelect a number from the list below:\n1) List all books\n2) Search book via title\n3) Search book via date\n4) Search book via author\n5) Add new book\n6) Exit\n")
        match user_input: 
            case '1':
                sif.list_books_interface(library1)
            case '2':
                sif.search_book_title_interface(library1)
            case '3':
                sif.search_book_date_interface(library1)
            case '4':
                sif.search_book_author_interface(library1)
            case '5':
                sif.add_book_interface(library1)
            case '6':
                break
def run():
    while True:
        user_input = input("\nWelcome Visitor, select a number from the list below:\n1) Member section\n2) Visitor book section\n3) Leave Library\n")
        match user_input:
            case '1':
                member_run()
            case '2':
                books_run()
            case '3':
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
                user_input = input(f"\nWelcome member {member_name}, select a number from the list below:\n1) Login as librarian\n2) Book section\n3) Borrow book\n4) Unborrow book\n5) Profile\n6) Logout\n")
                match user_input:
                    case '1':
                        librarian_run(user_input_ID)     
                    case '2':
                        books_run()
                    case '3':
                        sif.borrow_book_interface(library1, user_input_ID)
                    case '4':
                        sif.unborrow_book_interface(library1, user_input_ID)
                    case '5':
                        sif.profile_interface(library1, user_input_ID)
                    case '6':
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
                user_input = input(f"\nWelcome Librarian {member_name}, select a number from the list below:\n1)  Save books from file\n2)  Load books from file\n3) Delete book\n4)  Profile\n5)  Book section\n6)  Librarian section\n20) Logout\n")
                match user_input:
                    case '1':
                        sif.save_books_to_file_interface(library1)
                    case '2':
                        sif.load_books_from_file_interface(library1)
                    case '3':    
                        sif.delete_book_interface(library1)
                    case '4':
                        sif.profile_interface(library1, user_input_ID)
                    case '5':
                        books_run()
                    case '6':
                        librarian_interface()
                    case '7':
                        print("Logout successfully")
                        break
                    case _:
                        print("Not recognizable input, please select a number from the list provided.")
            case _:
                print("Wrong access")
                break
