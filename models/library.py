import models.member
import models.book

class Library:
    
    def __init__(self, name):
        self.name = name
        self.member_list = []
        self.book_list = []
        self.access_code = "777"

    def list_books(self):
        print("\nAll the books of the Library:")
        for book in self.book_list:
            print(f"{book} ")
        
    def list_members(self):
        print("\nAll the members of the Library:\n")
        for member in self.member_list:
            print(member)

    def register(self, name, birth, email, ID = None, librarian = False):
        member = models.member.Member(name, birth, email, ID, librarian)
        self.member_list.append(member)
        print(f"Member {member.name} succesfully registered into the Library")

    def delete_member(self, member_ID):
        member = self.find_member(member_ID)
        self.member_list.remove(member)
        print(f"Member {member.name} succesfully deleted from the Library")

    def modify_member(self):
        user_input_ID = input("Enter member ID to modify data")
        member = self.find_member(user_input_ID)
        print(member)
        user_input = input("Select data to modify:\n1) name\n2) email\n3) ID\n4) Librarian\n")
        match user_input:
            case '1':
                member.name = input("Enter new name: ")
            case '2':
                member.email = input("Enter new email: ")
            case '3':
                member.ID = input("Enter new ID: ")
            case '4':
                user_input_lib = input("Enter 'True' to give librarian access or 'False' to take away")
                member.is_librarian = user_input_lib == "True"

    def login(self, member_ID, member_email):
        for member in self.member_list:
            if member.ID == member_ID and member.email == member_email:
                print("Login succesful")
                return True, member.name
        return False, None
    
    def add_book(self, title, date, author):
        book = models.book.Book(title, date, author)
        self.book_list.append(book)
        print(f"Book {book.title} succesfully added to the Library")

    def find_member(self, member_ID):
         for member in self.member_list:
             if member.ID == member_ID:
                return member

    def borrow_book(self, borrow_book_title, member_ID):
        member = self.find_member(member_ID)
        for book in self.book_list:
            if book.title == borrow_book_title:
                member.borrowed_books.append(book)
                self.book_list.remove(book)
                print(f"Book {book.title} succesfully borrowed by member {member.name}")
    
    def unborrow_book(self, borrow_book_title, member_ID):
        member = self.find_member(member_ID)
        for book in member.borrowed_books:
            if book.title == borrow_book_title:
                member.borrowed_books.remove(book)
                self.book_list.append(book)
                print(f"Book {book.title} succesfully unborrowed by member {member.name}")
    
    def login_librarian(self, member_ID):
        member = self.find_member(member_ID)
        user_input_access_code = input("Enter Library access code: ")
        if user_input_access_code == self.access_code and member.is_librarian == True:
            print("Login succesful")
            return True, member.name
        else:
            return False, None

    def profile(self, member_ID):
        member = self.find_member(member_ID)
        borrowed_books = [f"{book.title}" for book in member.borrowed_books]
        print(f"Member => Name: {member.name}, Email: {member.email}, ID: {member.ID}, Librarian: {member.is_librarian}, Borrowed books: {borrowed_books}" )

    def save_members_to_file(self, filename):
        with open(filename, "w") as f:
            for member in self.member_list:
                f.write(f"{member.name},{member.birth},{member.email},{member.ID}, has librarian access: {member.is_librarian}, borrowed books: {'|'.join([book.title for book in member.borrowed_books])}\n")

    def save_books_to_file(self, filename):
        with open(filename, "w") as f:
            for book in self.book_list:
                f.write(f"{book.title},{book.date},{book.author}")


    def list_data(self):
        return f"Institute name: {self.name} \nMembers: {self.list_members()} \nBooks: {self.list_books()}"
    


