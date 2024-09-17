from Sale import Sale
from FileRepository import FileRepository

class SaleFileRepository(FileRepository):
	def __init__(self, fileName):
		super().__init__(fileName)

	def getAll(self):
		sales = []
		with open(self.fileName, "r") as f:
			for line in f:
				sales.append(Sale.fromString(line))
		return sales

	def saveAll(self, sales):
		with open(self.fileName, "w") as f:
			for sale in sales:
				f.write(str(sale) + "\n")

	def add(self, sale):
		sale.id = self.getNextId()
		with open(self.fileName, "a") as f:
			f.write(str(sale) + "\n")

	def getById(self, id):
		sales = self.getAll()
		for sale in sales:
			if sale.id == id:
				return sale
		return None

	def update(self, sale):
		self.updateLine(sale.id, str(sale))

	def delete(self, id):
		sales = self.getAll()
		for sale in sales:
			if sale.id == id:
				sales.remove(sale)
				break
		with open(self.fileName, "w") as f:
			for sale in sales:
				f.write(str(sale) + "\n")
