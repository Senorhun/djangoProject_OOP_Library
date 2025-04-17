
class Library:

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

    def list_data(self):
        return f"Institute name: {self.name} \nMembers: {self.list_members()} \nBooks: {self.list_books()}"
    

