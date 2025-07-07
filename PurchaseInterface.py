from datetime import date

from Purchase import Purchase
from Supplier import Supplier
from Product import Product

from Inventory import Inventory
from TextUtils import *

themeColor = BRIGHT_CYAN

def listPurchases(inventory:Inventory):
	clearScreen()
	printTitle("Listing purchases", themeColor)
	purchases = inventory.getPurchases()
	gotoxy(1,4)
	printColored(f"{"ID":3} {"Date":10} {"Supplier":30} {"Product":30} {"Quantity":10} {"Discount":10} {"Total"}", themeColor)
	for i in range(len(purchases)):
		p:Purchase = purchases[i]
		s:Supplier = inventory.getSupplierById(p.supplierId)
		pr:Product = inventory.getProductById(p.productId)
		gotoxy(1,5+i); print(f"{str(p.id):3} {p.date:10} {s.name:30} {pr.name:30} {str(p.quantity):10} {f"{p.discount}%":10} {p.total(pr.buyPrice):.2f}")
	input()

def addPurchase(inventory:Inventory):
	clearScreen()
	printTitle("Performing Purchase", themeColor) 
	purchaseDate = date.today().strftime("%d/%m/%Y")
	supplierId = input("Supplier ID: ")
	productId = input("Product ID: ")
	quantity = float(input("Quantity: "))
	discount = float(input("Discount: "))
	purchase = Purchase(0, purchaseDate, supplierId, productId, quantity, discount)
	inventory.addPurchase(purchase)
	input()

def deletePurchase(inventory:Inventory):
	clearScreen()
	printTitle("Deleting purchase", themeColor)
	id = input("Purchase ID: ")
	inventory.deletePurchase(id)
	input()