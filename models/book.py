

class Book:

    def __init__(self, title, date, author):
        self.title = title
        self.date = date
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, Date: {self.date}, Author: {self.author}"
