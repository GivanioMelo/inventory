from Product import Product
from Sale import Sale
from Purchase import Purchase
from Client import Client
from Supplier import Supplier

from ClientFileRepository import ClientFileRepository
from ProductFileRepository import ProductFileRepository
from PurchaseFileRepository import PurchaseFileRepository
from SaleFileRepository import SaleFileRepository
from SupplierFileRepository import SupplierFileRepository

class Inventory:
	def __init__(self):
		self.products = ProductFileRepository("products.txt")
		self.sales = SaleFileRepository("sales.txt")
		self.purchases = PurchaseFileRepository("purchases.txt")
		self.clients = ClientFileRepository("clients.txt")
		self.suppliers = SupplierFileRepository("suppliers.txt")

	def addProduct(self, product): self.products.add(product)
	def addSale(self, sale): self.sales.add(sale)
	def addPurchase(self, purchase): self.purchases.add(purchase)
	def updateProduct(self, product): self.products.update(product)
	def updateSale(self, sale): self.sales.update(sale)
	def updatePurchase(self, purchase): self.purchases.update(purchase)
	def deleteProduct(self, id): self.products.delete(id)
	def deleteSale(self, id): self.sales.delete(id)
	def deletePurchase(self, id): self.purchases.delete(id)
	def getProducts(self): return self.products.getAll()
	def getSales(self): return self.sales.getAll()
	def getPurchases(self): return self.purchases.getAll()
	def getProductById(self, id): return self.products.getById(id)
	def getSaleById(self, id): return self.sales.getById(id)
	def getPurchaseById(self, id): return self.purchases.getById(id)

	def getSalesByProduct(self, productId):
		sales = self.getSales()
		productSales = []
		for sale in sales:
			if sale.productId == productId:
				productSales.append(sale)
		return productSales

	def getPurchasesByProduct(self, productId):
		purchases = self.getPurchases()
		productPurchases = []
		for purchase in purchases:
			if purchase.productId == productId:
				productPurchases.append(purchase)
		return productPurchases

	def getTotalSpentByProduct(self, productId):
		product = self.getProductById(productId)
		purchases = self.getPurchasesByProduct(productId)
		total = 0
		for purchase in purchases:
			total += purchase.total(product.buyPrice)
		return total

	def getItensPurchasedByProduct(self, productId):
		purchases = self.getPurchasesByProduct(productId)
		total = 0
		for purchase in purchases:
			total += purchase.quantity
		return total

	def getItensSoldByProduct(self, productId):
		sales = self.getSalesByProduct(productId)
		total = 0
		for sale in sales:
			total += sale.quantity
		return total

	def getTotalSoldByProduct(self, productId):
		product = self.getProductById(productId)
		sales = self.getSalesByProduct(productId)
		total = 0
		for sale in sales:
			total += sale.total(product.sellPrice)
		return total

	def getStockByProduct(self, productId):
		stock = 0
		sales = self.getSalesByProduct(productId)
		purchases = self.getPurchasesByProduct(productId)
		for sale in sales:
			stock -= sale.quantity
		for purchase in purchases:
			stock += purchase.quantity
		return stock

	def getSalesByClient(self, clientId):
		sales = self.getSales()
		clientSales = []
		for sale in sales:
			if sale.clientId == clientId:
				clientSales.append(sale)
		return clientSales

	def getPurchasesBySupplier(self, supplierId):
		purchases = self.getPurchases()
		supplierPurchases = []
		for purchase in purchases:
			if purchase.supplierId == supplierId:
				supplierPurchases.append(purchase)
		return supplierPurchases

	def getClientById(self, clientId):
		client = self.clients.getById(clientId)
		return client

	def getSupplierById(self, supplierId):
		supplier = self.suppliers.getById(supplierId)
		return supplier