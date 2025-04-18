

def list_books_interface(library1):
    library1.list_books()

def register_interface(library1):
    print("Enter data to register:")
    name = input("Name: ")
    birth = input ("Date of birth: ")
    email = input("Email: ")
    library1.register(name, birth, email)
    print(library1.member_list[-1])

def login_interface(library1, user_input):
    return library1.login(user_input)