from item import *

class furniture(Item):

	def __init__(self, itemID, name, descr, bidInfo, age, material):
		Item.__init__(self, itemID, name, descr, bidInfo)
		self._age = age
		self._material = material

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self, age):
		self._age = age

	@property
	def material(self):
		return self._material

	@material.setter
	def material(self, material):
		self._material = material

	def __str__(self):
		return ("Item type: Furniture")