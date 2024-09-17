from Transaction import Transaction

class Purchase(Transaction):
	def __init__(self, id, date, supplierId, productId, quantity, discount):
		super().__init__(id, date, productId, quantity, discount)
		self.supplierId = supplierId
	def fromString(string):
		id, date, supplierId, productId, quantity, discount = string.split(",")
		return Purchase(int(id), date, int(supplierId), int(productId), float(quantity), float(discount))
	
	def __str__(self):
		return f"{self.id}, {self.date}, {self.supplierId}, {self.productId}, {self.quantity}, {self.discount}"

	def __repr__(self):
		return f"{self.id}, {self.date}, {self.supplierId}, {self.productId}, {self.quantity},{self.discount}"
	
	def __eq__(self, other):
		return self.__hash__() == other.__hash__()
	
	def __hash__(self):
		return hash(self.id, self.date, self.productId, self.supplierId)