
def list_books_interface(library1):
    library1.list_books()

def register_interface(library1):
    print("Enter data to register:")
    name = input("Name: ")
    birth = input ("Date of birth: ")
    email = input("Email: ")
    library1.register(name, birth, email)
    print(library1.member_list[-1])

def login_interface(library1, user_input_ID, user_input_email):
    return library1.login(user_input_ID, user_input_email)

def add_book(library1):
    user_input_title = input("Enter the book title: ")
    user_input_date = input("Enter the book date: ")
    user_input_author = input("Enter the book author: ")
    library1.add_book(user_input_title, user_input_date, user_input_author)

def borrow_book(library1, user_input_ID):
    user_input_title = input("Enter book's title: ")
    library1.borrow_book(user_input_title, user_input_ID)

def unborrow_book(library1, user_input_ID):
    user_input_title = input("Enter book's title: ")
    library1.unborrow_book(user_input_title, user_input_ID)

def profile(library1, user_input_ID):
    library1.profile(user_input_ID)