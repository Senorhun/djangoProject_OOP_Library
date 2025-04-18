import models.member

class Library:
    member_list = []

    def __init__(self, name, member_list, book_list):
        self.name = name
        self.member_list = member_list
        self.book_list = book_list
        self.access_code = 777

    def list_books(self):
        for book in self.book_list:
            print(f"Title: {book} ")
        
    def list_members(self):
        return ", ".join(self.member_list)

    def register(self, name, birth, email):
        member = models.member.Member(name, birth, email)
        self.member_list.append(member)

    def login(self, member_ID):
        for ID in models.member.Member.used_IDs:
            if ID == member_ID:
                return True
            
    def profile(self, member_ID):
        pass

    def list_data(self):
        return f"Institute name: {self.name} \nMembers: {self.list_members()} \nBooks: {self.list_books()}"
    


