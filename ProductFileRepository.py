from Product import Product
from FileRepository import FileRepository

class ProductFileRepository(FileRepository):
	def __init__(self, fileName):
		super().__init__(fileName)
	
	def getAll(self):
		products = []
		with open(self.fileName, "r") as f:
			for line in f:
				products.append(Product.fromString(line))
		return products
	def saveAll(self, data):
		with open(self.fileName, "w") as f:
			for product in data:
				f.write(str(product) + "\n")
	def add(self, product):
		product.id = self.getNextId()
		with open(self.fileName, "a") as f:
			f.write(str(product) + "\n")
	
	def update(self, product):
		self.updateLine(product.id, str(product))

	def delete(self, id):
		products = self.getAll()
		for product in products:
			if product.id == id:
				products.remove(product)
				break
		with open(self.fileName, "w") as f:
			for product in products:
				f.write(str(product) + "\n")
	
	def getById(self, id):
		products = self.getAll()
		for product in products:
			if product.id == id:
				return product
		return None