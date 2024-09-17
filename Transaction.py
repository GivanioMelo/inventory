class Transaction:
	def __init__(self, id, date, productId, quantity, discount):
		self.id = id
		self.date = date
		self.productId = productId
		self.quantity = quantity
		self.discount = discount
	
	def total(self, price = 0.0):
			return self.quantity * (price - self.discount)