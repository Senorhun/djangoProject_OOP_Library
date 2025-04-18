import models.member
import models.book

class Library:
    
    def __init__(self, name):
        self.name = name
        self.member_list = []
        self.book_list = []
        self.access_code = 777

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

   

    def profile(self, member_ID):
        pass

    def list_data(self):
        return f"Institute name: {self.name} \nMembers: {self.list_members()} \nBooks: {self.list_books()}"
    


