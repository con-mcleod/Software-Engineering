class bid(object):

	def __init__(self, time, userID, price):
		self._time = time
		self._userID = userID
		self._price = price

	@property
	def time(self):
		return self._time

	@time.setter
	def time(self, time):
		self._time = time

	@property
	def userID(self):
		return self._userID

	@userID.setter
	def userID(self, userID):
		self._userID = userID

	@property
	def price(self):
		return self._price

	@price.setter
	def price(self, price):
		self._price = price