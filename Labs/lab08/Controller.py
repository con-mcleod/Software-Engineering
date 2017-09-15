from LibraryModel import LibraryModel
from LibraryView import LibraryView

# Controller module
class Controller(object):

	def __init__ (self):
		pass


	def search_book (self, title):
		model = LibraryModel()
		view = LibraryView()
		book = model.search_book(title)
		return view.print_book(book, title)



	def search_author (self, author):
		model = LibraryModel()
		view = LibraryView()
		book_list = model.search_author(author)
		return view.print_author(book_list, author)