from Purchase import Purchase
from Supplier import Supplier
from Product import Product

from Inventory import Inventory

def listPurchases(inventory:Inventory):
	print("Listing purchases")
	purchases = inventory.getPurchases()
	for purchase in purchases:
		print(purchase)
	input()

def addPurchase(inventory:Inventory):
	print("Performing Purchase") 
	date = date.today().strftime("%d/%m/%Y")
	supplierId = input("Supplier ID: ")
	productId = input("Product ID: ")
	quantity = float(input("Quantity: "))
	discount = float(input("Discount: "))
	purchase = Purchase(0, date, supplierId, productId, quantity, discount)
	inventory.addPurchase(purchase)
	input()

def deletePurchase(inventory:Inventory):
	print("Deleting purchase")
	id = input("Purchase ID: ")
	inventory.deletePurchase(id)
	input()