class Transaction:
	def __init__(self, id, date, productId, quantity, discount):
		self.id = id
		self.date = date
		self.productId = productId
		self.quantity = quantity
		self.discount = discount
	
	def total(self):
			return self.quantity * (self.productId.sellPrice - self.discount)