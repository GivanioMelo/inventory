from Sale import Sale
from Product import Product
from Client import Client
from Inventory import Inventory

def listSales(inventory:Inventory):
	print("Listing sales")
	sales = inventory.getSales()
	for sale in sales:
		print(sale)

def addSale(inventory:Inventory):
	print("Performing Sale")
	date = date.today().strftime("%d/%m/%Y")
	clientId = input("Client ID: ")
	productId = input("Product ID: ")
	quantity = float(input("Quantity: "))
	discount = float(input("Discount: "))
	sale = Sale(0, date, clientId, productId, quantity, discount)
	inventory.addSale(sale)

def deleteSale(inventory:Inventory):
	print("Canceling sale")
	id = input("Sale ID: ")
	inventory.deleteSale(id)
