from Transaction import Transaction

class Sale(Transaction):
	def __init__(self, id, date,clientId,productId, quantity, discount):
		super().__init__(id, date, productId, quantity, discount)
		self.clientId = clientId
	
	def fromString(string):
		id, date, clientId, productId, quantity, discount = string.split(",")
		return Sale(id, date, clientId, productId, float(quantity), float(discount))
	
	def __str__(self):
		return f"{self.id},{self.date},{self.clientId},{self.productId},{self.quantity},{self.discount}"

	def __repr__(self):
		return f"{self.id},{self.date},{self.clientId},{self.productId},{self.quantity},{self.discount}"
	
	def __eq__(self, other):
		return self.__hash__() == other.__hash__()
	
	def __hash__(self):
		return hash(self.id, self.date, self.productId, self.clientId)