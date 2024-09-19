from Inventory import Inventory

from TextUtils import *
import ProductInterface
import ClientInterface
import SupplierInterface
import SaleInterface
import PurchaseInterface

def drawScreen():
	clearScreen()
	printTitle(" Inventory Management System ",GREEN,WHITE)
	drawInfoBox()

	drawBox(1,4,24,7,BLUE)
	gotoxy(2,4); print(" Products ")
	gotoxy(3,5); printBlue("01 - List All")
	gotoxy(3,6); printBlue("02 - Add New")
	gotoxy(3,7); printBlue("03 - Update")
	gotoxy(3,8); printBlue("04 - Delete ")
	gotoxy(3,9); printBlue("05 - Details")
	
	drawBox(25,4,24,7,RED)
	gotoxy(26,4); print(" Clients ")
	gotoxy(26,5); printRed("11 - List All")
	gotoxy(26,6); printRed("12 - Add New")
	gotoxy(26,7); printRed("13 - Update")
	gotoxy(26,8); printRed("14 - Delete ")
	gotoxy(26,9); printRed("15 - Details")

	drawBox(49,4,24,7,YELLOW)
	gotoxy(50,4); print(" Suppliers ")
	gotoxy(51,5); printYellow("21 - List All")
	gotoxy(51,6); printYellow("22 - Add New")
	gotoxy(51,7); printYellow("23 - Update")
	gotoxy(51,8); printYellow("24 - Delete ")
	gotoxy(51,9); printYellow("25 - Details")

	drawBox(73,4,24,7,BRIGHT_MAGENTA)
	gotoxy(74,4); print("Sales")
	gotoxy(75,5); printBrightMagenta("31 - List All")
	gotoxy(75,6); printBrightMagenta("32 - Add New")
	gotoxy(75,7); printBrightMagenta("33 - Cancel")
	
	drawBox(97,4,24,7,BRIGHT_CYAN)
	gotoxy(98,4); print("Purchases")
	gotoxy(99,5); printBrightCyan("41 - List All")
	gotoxy(99,6); printBrightCyan("42 - Add New")
	gotoxy(99,7); printBrightCyan("43 - Cancel")

	drawBox(1,11,120,3, LIGHT_GRAY)
	gotoxy(2,12); printLightGray("00 - Exit")
	
	drawBox(1,14,120,3, LIGHT_GRAY)

def mainMenu(inventory:Inventory):
	while True:
		drawScreen()
		gotoxy(2,15); option = input("Input an option: ")

		if option == "0" or option == "00": break

		elif option == "01": ProductInterface.listProducts(inventory)
		elif option == "02": ProductInterface.addProduct(inventory)
		elif option == "03": ProductInterface.updateProduct(inventory)
		elif option == "04": ProductInterface.deleteProduct(inventory)
		elif option == "05": ProductInterface.printProductDetails(inventory)

		elif option == "11": ClientInterface.listClients(inventory)
		elif option == "12": ClientInterface.addClient(inventory)
		elif option == "13": ClientInterface.updateClient(inventory)
		elif option == "14": ClientInterface.deleteClient(inventory)
		elif option == "15": ClientInterface.printClientDetails(inventory)

		elif option == "21": SupplierInterface.listSuppliers(inventory)
		elif option == "22": SupplierInterface.addSupplier(inventory)
		elif option == "23": SupplierInterface.updateSupplier(inventory)
		elif option == "24": SupplierInterface.deleteSupplier(inventory)
		elif option == "25": SupplierInterface.printSupplierDetails(inventory)

		elif option == "31": SaleInterface.listSales(inventory)
		elif option == "32": SaleInterface.addSale(inventory)
		elif option == "33": SaleInterface.deleteSale(inventory)

		elif option == "41": PurchaseInterface.listPurchases(inventory)
		elif option == "42": PurchaseInterface.addPurchase(inventory)
		elif option == "43": PurchaseInterface.deletePurchase(inventory)
		
		else:
			drawInfoBox("Invalid option, try again!", RED)
			input()

def auth():
	error = ""
	while True:
		clearScreen()
		printTitle(" Insert Authentication Key ",GREEN)
		drawInfoBox(error, RED)
		gotoxy(2,4); key = input()
		if key != "banana":
			error = "Access Denied! Input the correct authentication key..."
		else:
			printGreen("Access Granted! Wellcome...")
			drawInfoBox(" "*118)
			input()
			return

auth()
inventory = Inventory()
mainMenu(inventory)