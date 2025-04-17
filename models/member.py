from models.person import Person

class Member(Person):

    def __init__(self, name, birth, email, ID):
        super().__init__(name, birth)
        self.email = email
        self.ID = ID

    def __str__(self):
        return f"Member, {super().__str__()}, Email: {self.email}, ID: {self.ID}" 