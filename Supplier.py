from Contact import Contact

class Supplier(Contact):
	def __init__(self, id, name, email, phone):
		super().__init__(id, name, email, phone)