from models.member import Member

class Librarian(Member):
    
    def __init__(self, name, birth, email, ID, password):
        super().__init__(name, birth, email, ID)
        self.password = password

    def __str__(self):
        return f"Librarian-{super().__str__()}"