from models.library import Library
from models.book import book_list, Book
from models.person import people_list, Person
from models.member import Member
from models.librarian import Librarian

library1 = Library("Library", people_list, book_list)
print("\nWelcome to the Library")

book1 = Book("title", 1995, "writer")
person1 = Person("Bono", 1990)
member1 = Member("Bono", 1990, "bono@", 123)
librarian1 = Librarian("Juno", 1993, "juno@", 123, "pass")

def run():
    while True:
        user_input = input("\nSelect a number from the list below:\n1) Browsing books\n2) Login as member\n3) Add book to Library\n4) Leave Library\n")
        match user_input:
            case '1':
                print(library1.list_books())
            case '2':
                pass
            case '3':
                pass
            case '4':
                print("Thank you for visiting, have a nice day!")
                break
            case _ :
                print("Not recognizable input, please select a number form the list provided.")