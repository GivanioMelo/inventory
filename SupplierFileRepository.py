from Supplier import Supplier
from FileRepository import FileRepository

class SupplierFileRepository(FileRepository):
	def __init__(self, fileName):
		super().__init__(fileName)
	
	def getAll(self):
		suppliers = []
		with open(self.fileName, "r") as f:
			for line in f:
				suppliers.append(Supplier.fromString(line))
		return suppliers

	def saveAll(self, suppliers):
		with open(self.fileName, "w") as f:
			for supplier in suppliers:
				f.write(str(supplier) + "\n")

	def add(self, supplier):
		supplier.id = self.getNextId()
		with open(self.fileName, "a") as f:
			f.write(str(supplier) + "\n")

	def getById(self, id):
		suppliers = self.getAll()
		for supplier in suppliers:
			if supplier.id == id:
				return supplier
		return None

	def update(self, supplier):
		self.updateLine(supplier.id, str(supplier)) 

	def delete(self, id):
		suppliers = self.getAll()
		for supplier in suppliers:
			if supplier.id == id:
				suppliers.remove(supplier)
				break 
		with open(self.fileName, "w") as f:
			for supplier in suppliers:
				f.write(str(supplier) + "\n")