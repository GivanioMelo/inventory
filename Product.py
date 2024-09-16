class Product:
	def __init__(self, id=0, name="", buyPrice=0, sellPrice=0):
		self.id = id
		self.name = name
		self.buyPrice = buyPrice
		self.sellPrice = sellPrice
	
	def fromString(string):
		id, name, buyPrice, sellPrice = string.split(", ")
		return Product(int(id), name, float(buyPrice), float(sellPrice))
	
	def __str__(self):
		return f"{self.id}, {self.name}, {self.buyPrice}, {self.sellPrice}"

	def __repr__(self):
		return f"{self.id}, {self.name}, {self.buyPrice}, {self.sellPrice}"
	
	def __eq__(self, other):
		return self.__hash__() == other.__hash__()
	
	def __hash__(self):
		return hash(self.id, self.name, self.buyPrice, self.sellPrice)