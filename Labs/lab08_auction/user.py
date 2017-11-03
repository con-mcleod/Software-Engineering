class user(object):

	def __init__(self, userID, name, postedItems, bids):
		self._userID = userID
		self._name = name
		self._postedItems = postedItems

	@property
	def userID(self):
		return self._userID

	@userID.setter
	def userID(self, userID):
		self._userID = userID

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name