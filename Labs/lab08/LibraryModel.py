import sqlite3

# Model
class LibraryModel(object):
	def search_author(self, author):
		query = "SELECT title, year, genre from BOOK where author = '%s'" % author
		book_list = self._dbselect(query)
		return book_list

	def search_book(self, title):
		query = "SELECT title, author, year, genre from BOOK where title = '%s'" % title
		book = self._dbselect(query)
		return book

	def _dbselect(self, query):
		# Logic to connect to the database
		connection = sqlite3.connect('library.db')
		cursorObj = connection.cursor()
		# execute the query
		rows = cursorObj.execute(query)
		connection.commit()
		results = []
		for row in rows:
			results.append(row)
			cursorObj.close()
			return results