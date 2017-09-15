#View
class LibraryView(object):
	def print_author(self, book_list, author):
		print ("####################################")
		print("%s's books:"%author)
		print ("____________________________________")
		for book in book_list:
			print(book)
			print("\n")
	def print_book(self, book, title):
		print ("####################################")
		print("Book with title: %s"%title)
		print ("____________________________________")
		print(book)
		print ("\n")