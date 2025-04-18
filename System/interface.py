from models.library import Library
from models.book import book_list, Book
from models.person import people_list, Person
from models.member import Member

library1 = Library("Library", people_list, book_list)
print("\nWelcome to the Library")

book1 = Book("title", 1995, "writer")
person1 = Person("Bono", 1990)
member1 = Member("Bono1", 1990, "bono@")
member2 = Member("Bono2", 1990, "bono@")
member3 = Member("Bono3", 1990, "bono@")
member4 = Member("Bono4", 1990, "bono@")
member5 = Member("Bono5", 1990, "bono@")

def run():
    while True:
        user_input = input("\nSelect a number from the list below:\n1) Browsing books\n2) Login as member\n3) Register as new member\n4) Leave Library\n")
        match user_input:
            case '1':
                print(library1.list_books())
            case '2':
                user_input = input("\nEnter member ID to access:\n")
                user_input_access = library1.login(user_input)
                match user_input_access:
                    case True:
                        print("Successfull login")
                    case _:
                        print("Wrong access ID")
            case '3':
                print("Enter data to register:")
                name = input("Name: ")
                birth = input ("Date of birth: ")
                email = input("Email: ")
                library1.register(name, birth, email)
                print(library1.member_list[-1])
            case '4':
                print("Thank you for visiting, have a nice day!")
                break
            case _ :
                print("Not recognizable input, please select a number form the list provided.")