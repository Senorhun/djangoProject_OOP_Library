from Institute import library
from Data.books import book_list
from Data.people import people_list

library1 = library.Library("Library", people_list, book_list)
print("lets start")
print(library1.list_data())