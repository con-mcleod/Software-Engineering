from user import user
from bid import bid
from item import item


class auctionSys(object):

	def __init__(self):
		self._userPool = self.populateUsers()
		self._itemPool = self.populateItems()

	def populateUsers(self):
		pass

	def populateItems(self):
		pass
