from Client import Client
from Product import Product
from Purchase import Purchase
from Sale import Sale
from Supplier import Supplier

from Inventory import Inventory

from TextColors import *
from TextUtils import *

def printTitle(text:str, boxColor = WHITE, textColor = WHITE):
	x = 60 - (int(len(text)/2))
	drawBox(1,1,120,3,boxColor)
	gotoxy(x,2)
	print(text)

def drawEditField(text:str, line:int, boxColor = WHITE, textColor = WHITE):
	drawBox(1,line,20,3,boxColor)
	drawBox(21,line,100,3,boxColor)
	gotoxy(2,line+1)
	printColored(text,textColor)

def drawInfoBox(text:str = "", textColor = WHITE):
	drawBox(1,27,120,3,DARK_GRAY)
	gotoxy(2,28)
	printColored(text, textColor)

# ------------------
# ---- Products ----
# ------------------
def listProducts(inventory:Inventory):
	clearScreen()
	printTitle(" Listing products ", BLUE, WHITE)

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
	printTitle(" Adding new product ", BLUE, WHITE)
	drawEditField("Name: ", line=4, boxColor=BLUE, textColor=WHITE)
	drawEditField("Buy Price (R$): ", line=7, boxColor=BLUE, textColor=WHITE)
	drawEditField("Sell Price (R$): ", line=10, boxColor=BLUE, textColor=WHITE)
	drawInfoBox()

	gotoxy(22,5);  name = input()
	gotoxy(22,8);  buyPrice = float(input())
	gotoxy(22,11); sellPrice = float(input())

	product = Product(0, name, buyPrice, sellPrice)
	inventory.addProduct(product)
	input()

def updateProduct(inventory:Inventory):
	clearScreen()
	drawBox(1,27,120,3,DARK_GRAY)

	printTitle(" Updating product ", BLUE, WHITE)
	drawEditField("Product Id:", line=4, boxColor=BLUE, textColor=WHITE)
	drawEditField("Name: ", line=7, boxColor=BLUE, textColor=WHITE)
	drawEditField("Buy price: ", line=10, boxColor=BLUE, textColor=WHITE) 
	drawEditField("Sell price: ", line=13, boxColor=BLUE, textColor=WHITE)

	productExists = False
	while not productExists:
		gotoxy(22,5); id = int(input())
		selectedProduct = inventory.getProductById(id)
		if selectedProduct is None:
			gotoxy(2,28); printRed("Product doesn't exist, please insert a valid id!")
		else:
			productExists = True
			gotoxy(22,8);  printDarkGray(selectedProduct.name)
			gotoxy(22,11); printDarkGray(f"{selectedProduct.buyPrice:.2f}")
			gotoxy(22,14); printDarkGray(f"{selectedProduct.sellPrice:.2f}")
			break
	gotoxy(22,8);  name = input()
	gotoxy(22,11); buyPrice = float(input())
	gotoxy(22,14); sellPrice = float(input())
	
	product = Product(id, name, buyPrice, sellPrice)
	inventory.updateProduct(product)

	gotoxy(2,28); print("Product sucessfully updated! Press ENTER to proceed...")
	input()

def deleteProduct(inventory:Inventory):
	drawBox(21,10,100,3,DARK_GRAY)

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
		printTitle(" Inventory Management System ",GREEN,WHITE)
		drawInfoBox()

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
		
		else:
			drawInfoBox("Invalid option, try again!", RED)
			input()

inventory = Inventory()
mainMenu(inventory)