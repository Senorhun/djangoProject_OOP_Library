
book_list = [
    "The Shadow of Eternity",
    "Echoes in the Mist",
    "The Clockwork Kingdom",
    "Whispers of the Forgotten",
    "Beneath Crimson Skies",
    "The Last Ember",
    "Tides of Destiny",
    "The Glass Labyrinth",
    "Chronicles of the Starborn",
    "Song of the Hollow Wind"
]

class Book:

    def __init__(self, title, date, author):
        self.title = title
        self.date = date
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, Date: {self.date}, Author: {self.author}"
