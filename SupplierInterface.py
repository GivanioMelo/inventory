
from Supplier import Supplier
from Purchase import Purchase
from Product import Product
from Inventory import Inventory

def listSuppliers(inventory:Inventory):
	print("Listing suppliers")
	suppliers = inventory.getSuppliers()
	for supplier in suppliers:
		print(supplier)

def addSupplier(inventory:Inventory):
	print("Adding new supplier")
	name = input("Name: ")
	email = input("Email: ")
	phone = input("Phone: ")
	supplier = Supplier(0, name, email, phone)
	inventory.addSupplier(supplier)
	input()

def updateSupplier(inventory:Inventory):
	print("Updating supplier")
	id = input("Supplier ID: ")
	name = input("Name: ")
	email = input("Email: ")
	phone = input("Phone: ")
	supplier = Supplier(id, name, email, phone)
	inventory.updateSupplier(supplier)

def deleteSupplier(inventory:Inventory):
	print("Deleting supplier")
	id = input("Supplier ID: ")
	inventory.deleteSupplier(id)

def printSupplierDetails(inventory:Inventory):
	print("Printing supplier details")
	id = input("Supplier ID: ")
	supplier = inventory.getSupplierById(id)
	print(supplier)

	print("Purchases:")
	purchases = inventory.getPurchasesBySupplier(id)
	for purchase in purchases:
		print(purchase)
