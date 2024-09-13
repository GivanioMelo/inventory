from Client import Client
from Product import Product
from Purchase import Purchase
from Sale import Sale
from Supplier import Supplier

from Inventory import Inventory

from TextColors import *
from TextUtils import *

# ------------------
# ---- Products ----
# ------------------
def listProducts(inventory:Inventory):
	clearScreen()
	drawBox(1,1,120,3,BLUE)	
	gotoxy(50,2); print("Listing products")

	products = inventory.getProducts()
	h = len(products) + 3

	drawBox(1,4,120,h,BLUE)
	gotoxy(2,5); printBrightBlue(f"{'Id':5} | {'Name':50} |    {'Buy price':10} |    {'Sell Price':10}")
	for i in range(len(products)):
		p:Product = products[i]
		gotoxy(2,6+i); printBrightBlue(f"{p.id:5} | {p.name:50} | R$ {p.buyPrice:10.2f} | R$ {p.sellPrice:10.2f}")
	gotoxy(1,4+h+1); input()

def addProduct(inventory:Inventory):
	clearScreen()
	drawBox(1,1,120,3,BLUE)	
	drawBox(1,4,20,3,BLUE)	; drawBox(21,4,100,3,BLUE)
	drawBox(1,7,20,3,BLUE)	; drawBox(21,7,100,3,BLUE)
	drawBox(1,10,20,3,BLUE)	; drawBox(21,10,100,3,BLUE)
	
	gotoxy(50,2); print("Adding new product")
	gotoxy(2,5);  print("Name:")
	gotoxy(2,8);  print("Buy Price (R$): ")
	gotoxy(2,11); print("Sell Price (R$): ")

	gotoxy(22,5);  name = input()
	gotoxy(22,8);  buyPrice = float(input())
	gotoxy(22,11); sellPrice = float(input())

	product = Product(0, name, buyPrice, sellPrice)
	inventory.addProduct(product)
	input()

def updateProduct(inventory:Inventory):
	print("Updating product")
	id = input("Product ID: ")
	name = input("Name: ")
	buyPrice = float(input("Buy price: "))
	sellPrice = float(input("Sell price: "))
	product = Product(id, name, buyPrice, sellPrice)
	inventory.updateProduct(product)
	input()

def deleteProduct(inventory:Inventory):
	print("Deleting product")
	id = input("Product ID: ")
	inventory.deleteSalesByProduct(id)
	inventory.deletePurchasesByProduct(id)
	inventory.deleteProduct(id)

	input()

def printProductDetails(inventory:Inventory):
	print("Printing product details")
	id = input("Product ID: ")
	product = inventory.getProductById(id)
	print(product)
	
	print("Sales:")
	sales = inventory.getSalesByProduct(id)
	for sale in sales:
		print(sale)
	print("Total sold: ", inventory.getTotalSoldByProduct(id))

	print("Purchases:")
	purchases = inventory.getPurchasesByProduct(id)
	for purchase in purchases:
		print(purchase)
	print("Total spent: ", inventory.getTotalSpentByProduct(id))
	print("Stock: ", inventory.getStockByProduct(id))

	input()

# -----------------
# ---- Clients ----
# -----------------
def listClients(inventory:Inventory):
    print("Listing clients")
    clients = inventory.getClients()
    for client in clients:
        print(client)

def addClient(inventory:Inventory):
    print("Adding new client")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    client = Client(0, name, email, phone)
    inventory.addClient(client)

def updateClient(inventory:Inventory):
    print("Updating client")
    id = input("Client ID: ")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    client = Client(id, name, email, phone)
    inventory.updateClient(client)

def deleteClient(inventory:Inventory):
    print("Deleting client")
    id = input("Client ID: ")
    inventory.deleteClient(id)

def printClientDetails(inventory:Inventory):
    print("Printing client details")
    id = input("Client ID: ")
    client = inventory.getClientById(id)
    print(client)
    print("Sales:")
    sales = inventory.getSalesByClient(id)
    for sale in sales:
        print(sale)

# ---------------------
# ----- Suppliers -----
# ---------------------
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

# -----------------
# ----- Sales -----
# -----------------
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

def mainMenu(inventory:Inventory):
	while True:
		clearScreen()
		drawBox(1,1,120,3,GREEN)
		gotoxy(44,2)
		print("Inventory Management System")
		
		drawBox(1,4,24,7,BLUE)
		gotoxy(2,4); print(" Products ")
		gotoxy(3,5); printBlue("01 - List All ")
		gotoxy(3,6); printBlue("02 - Add New")
		gotoxy(3,7); printBlue("03 - Update")
		gotoxy(3,8); printBlue("04 - Delete ")
		gotoxy(3,9); printBlue("05 - Details")
		
		drawBox(25,4,24,7,RED)
		gotoxy(26,4); print(" Clients ")
		gotoxy(26,5); printRed("11 - List All ")
		gotoxy(26,6); printRed("12 - Add New")
		gotoxy(26,7); printRed("13 - Update")
		gotoxy(26,8); printRed("14 - Delete ")
		gotoxy(26,9); printRed("15 - Details")

		drawBox(49,4,24,7,YELLOW)
		gotoxy(50,4); print(" Suppliers ")
		gotoxy(51,5); printYellow("21 - List All ")
		gotoxy(51,6); printYellow("22 - Add New")
		gotoxy(51,7); printYellow("23 - Update")
		gotoxy(51,8); printYellow("24 - Delete ")
		gotoxy(51,9); printYellow("25 - Details")

		drawBox(73,4,24,7,BRIGHT_MAGENTA)
		gotoxy(74,4); print("Sales")
		gotoxy(75,5); printBrightMagenta("31 - List All ")
		gotoxy(75,6); printBrightMagenta("32 - Add New")
		gotoxy(75,7); printBrightMagenta("33 - Cancel")
		
		drawBox(97,4,24,7,BRIGHT_CYAN)
		gotoxy(98,4); print("Purchases")
		gotoxy(99,5); printBrightCyan("41 - List All ")
		gotoxy(99,6); printBrightCyan("42 - Add New")
		gotoxy(99,7); printBrightCyan("43 - Cancel")

		drawBox(1,11,120,3, LIGHT_GRAY)
		gotoxy(2,12); printLightGray("00 - Exit")
		
		drawBox(1,14,120,3, LIGHT_GRAY)
		gotoxy(2,15); option = input("Input an option: ")

		if option == "0" or option == "00": break

		elif option == "01": listProducts(inventory)
		elif option == "02": addProduct(inventory)
		elif option == "03": updateProduct(inventory)
		elif option == "04": deleteProduct(inventory)
		elif option == "05": printProductDetails(inventory)

		elif option == "11": listClients(inventory)
		elif option == "12": addClient(inventory)
		elif option == "13": updateClient(inventory)
		elif option == "14": deleteClient(inventory)
		elif option == "15": printClientDetails(inventory)

		elif option == "21": listSuppliers(inventory)
		elif option == "22": addSupplier(inventory)
		elif option == "23": updateSupplier(inventory)
		elif option == "24": deleteSupplier(inventory)
		elif option == "25": printSupplierDetails(inventory)

		elif option == "31": listSales(inventory)
		elif option == "32": addSale(inventory)
		elif option == "33": deleteSale(inventory)

		elif option == "41": listPurchases(inventory)
		elif option == "42": addPurchase(inventory)
		elif option == "43": deletePurchase(inventory)

inventory = Inventory()
mainMenu(inventory)