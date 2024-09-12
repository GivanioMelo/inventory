class Product:
	def __init__(self, id, name, buyPrice, sellPrice):
		self.id = 0
		self.name = name
		self.buyPrice = buyPrice
		self.sellPrice = sellPrice
	
	def fromString(self, string):
		id, name, buyPrice, sellPrice = string.split(",")
		return Product(id, name, float(buyPrice), float(sellPrice))
	
	def __str__(self):
		return f"{self.id},{self.name},{self.buyPrice},{self.sellPrice}"

	def __repr__(self):
		return f"{self.id},{self.name},{self.buyPrice},{self.sellPrice}"
	
	def __eq__(self, other):
		return self.__hash__() == other.__hash__()
	
	def __hash__(self):
		return hash(self.id, self.name, self.buyPrice, self.sellPrice)