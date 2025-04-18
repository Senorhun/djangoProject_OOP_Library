from models.person import Person
import random, string

class Member(Person):
    used_IDs = set()
    

    def __init__(self, name, birth, email, ID = None, librarian = False):
        super().__init__(name, birth)
        self.email = email
        self.is_librarian = librarian
        self.ID = ID if ID is not None else self.generate_id()

    def generate_id(self):
        unique_id = f"{str(random.randint(1000,9999))}-{"".join(random.choices(string.ascii_uppercase, k=2))}"
        while True:
            if unique_id not in Member.used_IDs:
                Member.used_IDs.add(unique_id)
                return unique_id

    def __str__(self):
        return f"Member => {super().__str__()}, Email: {self.email}, ID: {self.ID}, Librarian: {self.is_librarian}" 