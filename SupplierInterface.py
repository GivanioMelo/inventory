
from Supplier import Supplier
from Purchase import Purchase
from Product import Product
from Inventory import Inventory
from TextUtils import *

themeColor = YELLOW

def listSuppliers(inventory:Inventory):
	clearScreen()
	printTitle(" Listing Suppliers ", themeColor)
	suppliers = inventory.getSuppliers()
	gotoxy(1,4)
	printColored(f"   {"ID":10} {"Name":30} {"E-mail":30} {"Phone":20}",themeColor)
	for i in range(len(suppliers)):
		s: Supplier = suppliers[i]
		print(f"   {str(s.id):10} {s.name:30} {s.email:30} {s.phone:20}")
	input()

def addSupplier(inventory:Inventory):
	clearScreen()
	printTitle(" Adding new supplier ",themeColor)
	
	gotoxy(2,4); printColored("Name: ",themeColor,end=""); name = input()
	if name == "": drawInfoBox("ERROR - Invalid Input, returning to menu...", RED); input(); return
	
	gotoxy(2,5); printColored("Email: ",themeColor,end=""); email = input()
	if email == "": drawInfoBox("ERROR - Invalid Input, returning to menu...", RED); input(); return
	
	gotoxy(2,6); printColored("Phone: ",themeColor,end=""); phone = input()
	if phone == "": drawInfoBox("ERROR - Invalid Input, returning to menu...", RED); input(); return

	supplier = Supplier(0, name, email, phone)
	inventory.addSupplier(supplier)
	input()

def updateSupplier(inventory:Inventory):
	clearScreen()
	printTitle(" Updating supplier ",themeColor)
	while True:
		try:
			gotoxy(2,4); printColored("Client ID: ",themeColor,end=""); id = input()
			id = int(id)
			s:Supplier = inventory.getClientById(id)
			gotoxy(2,5); printDarkGray(f"[{s.id}] {s.name} ({s.email} / {s.phone})")
			break
		except: drawInfoBox("ERROR - didn't input a valid ID... please try again")

	gotoxy(2,7); printColored("Name: ",themeColor,end=""); name = input()
	if name == "": drawInfoBox("ERROR - Invalid Input, returning to menu...", RED); input(); return
	gotoxy(2,8); printColored("Email: ",themeColor,end=""); email = input()
	if email == "": drawInfoBox("ERROR - Invalid Input, returning to menu...", RED); input(); return
	gotoxy(2,9); printColored("Phone: ",themeColor,end=""); phone = input()
	if phone == "": drawInfoBox("ERROR - Invalid Input, returning to menu...", RED); input(); return
	try: 
		s = Supplier(id, name, email, phone)
		inventory.updateSupplier(s)
		drawInfoBox("SUCCESS - supplier data updated... ", GREEN)
	except:
		drawInfoBox("ERROR - supplier update failed... ", RED)
	input()

def deleteSupplier(inventory:Inventory):
	clearScreen()
	print("Deleting supplier")
	id = input("Supplier ID: ")
	inventory.deleteSupplier(id)
	input()

def printSupplierDetails(inventory:Inventory):
	clearScreen()
	print("Printing supplier details")
	id = input("Supplier ID: ")
	supplier = inventory.getSupplierById(id)
	print(supplier)

	print("Purchases:")
	purchases = inventory.getPurchasesBySupplier(id)
	for purchase in purchases:
		print(purchase)
	input()
