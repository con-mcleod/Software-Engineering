#from electronics import electronics
#from furniture import furniture
#from book import Book

class Item(object):

	def __init__(self, itemID, name, descr, bidList):
		self._itemID = itemID
		self._name = name
		self._descr = descr

	@property
	def itemID(self):
		return self._itemID

	@itemID.setter
	def itemID(self, itemID):
		self._itemID = itemID




book1 = Book(1, "Harry Pot", "Wizard Book", [], "Rowling", 1996)
print (book1)
print ("Item ID: %s" %(book1.itemID))
print ("Author: %s" %(book1.author))
# print ("Item description: %s" %(book1.descr))
# print bid info set
print ("Date published: %s" %(book1.datePublished))




