
people_list = []

class Person:

    def __init__(self, name, birth):
        self.name = name
        self.birth = birth

    def __str__(self):
        return f"Name: {self.name}, Birth: {self.birth}"