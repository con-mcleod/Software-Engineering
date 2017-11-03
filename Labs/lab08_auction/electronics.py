from item import *

class electronics(Item):

	def __init__(self, itemID, name, descr, bidInfo, voltage, brand):
		Item.__init__(self, itemID, name, descr, bidInfo)
		self._voltage = voltage
		self._brand = brand

	@property
	def voltage(self):
		return self._voltage

	@voltage.setter
	def voltage(self, voltage):
		self._voltage = voltage

	@property
	def brand(self):
		return self._brand

	@brand.setter
	def brand(self, brand):
		self._brand = brand

	def __str__(self):
		return ("Item type: Electronics")