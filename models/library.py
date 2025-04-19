import models.member
import models.book

class Library:
    
    def __init__(self, name):
        self.name = name
        self.member_list = []
        self.book_list = []
        self.access_code = "777"

    def list_books(self):
        for book in self.book_list:
            print(f"Title: {book} ")
        
    def list_members(self):
        for member in self.member_list:
            print(member)

    def register(self, name, birth, email, ID = None, librarian = False):
        member = models.member.Member(name, birth, email, ID, librarian)
        self.member_list.append(member)

    def login(self, member_ID, member_email):
        for member in self.member_list:
            if member.ID == member_ID and member.email == member_email:
                return True
        return False
    
    def add_book(self, title, date, author):
        book = models.book.Book(title, date, author)
        self.book_list.append(book)

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
    
   

    def profile(self, member_ID):
        member = self.find_member(member_ID)
        borrowed_books = [f"{book.title}" for book in member.borrowed_books]
        print(f"Member => Name: {member.name}, Email: {member.email}, ID: {member.ID}, Librarian: {member.is_librarian}, Borrowed books: {borrowed_books}" )

    def list_data(self):
        return f"Institute name: {self.name} \nMembers: {self.list_members()} \nBooks: {self.list_books()}"
    


