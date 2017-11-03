from item import *

class Book(Item):

	def __init__(self, itemID, name, descr, bidInfo, author, datePublished):
		Item.__init__(self, itemID, name, descr, bidInfo)
		self._author = author
		self._datePublished = datePublished

	@property
	def author(self):
		return self._author

	@author.setter
	def author(self, author):
		self._author = author

	@property
	def datePublished(self):
		return self._datePublished

	@datePublished.setter
	def datePublished(self, datePublished):
		self._datePublished = datePublished

	def __str__(self):
		return ("Item type: Book")