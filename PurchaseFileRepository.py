from Purchase import Purchase
from FileRepository import FileRepository

class PurchaseFileRepository(FileRepository):
	def __init__(self, fileName):
		super().__init__(fileName)
	def getAll(self):
		purchases = []
		with open(self.fileName, "r") as f:
			for line in f:
				purchases.append(Purchase.fromString(line))
	def saveAll(self, purchases):
		with open(self.fileName, "w") as f:
			for purchase in purchases:
				f.write(str(purchase) + "\n")
	def add(self, purchase):
		purchase.id = self.getNextId()
		with open(self.fileName, "a") as f:
			f.write(str(purchase) + "\n")
	def getById(self, id):
		purchases = self.getAll()
		for purchase in purchases:
			if purchase.id == id:
				return purchase
		return None
	def update(self, purchase):
		self.updateLine(purchase.id, str(purchase))
	def delete(self, id):
		purchases = self.getAll
		for purchase in purchases:
			if purchase.id == id:
				purchases.remove(purchase)
				break
		with open(self.fileName, "w") as f:
			for purchase in purchases:
				f.write(str(purchase) + "\n")