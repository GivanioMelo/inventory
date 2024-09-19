from datetime import date

from Sale import Sale
from Product import Product
from Client import Client
from Inventory import Inventory
from TextUtils import *

themeColor = BRIGHT_MAGENTA

def listSales(inventory:Inventory):
	clearScreen()
	printTitle("Listing sales", themeColor)
	sales = inventory.getSales()
	gotoxy(1,4)
	printColored(f"{"ID":3} {"Date":10} {"Client":30} {"Product":30} {"Quantity":10} {"Discount":10} {"Total"}", themeColor)
	for i in range(len(sales)):
		s:Sale = sales[i]
		c:Client = inventory.getClientById(s.clientId)
		p:Product = inventory.getProductById(s.productId)
		gotoxy(1,5+i); print(f"{s.id:3} {s.date:10} {c.name:30} {p.name:30} {str(s.quantity):10} {f"{s.discount}%":10} {s.total(p.sellPrice):.2f}")
	input()

def addSale(inventory:Inventory):
	clearScreen()
	printTitle("Performing Sale", themeColor)
	saleDate = date.today().strftime("%d/%m/%y")

	try:
		gotoxy(1,4); printColored("Client ID:  ", themeColor); 	clientId = int(input())
		client:Client = inventory.getClientById(clientId)
		gotoxy(5,5); printDarkGray(client)
	except:
		drawInfoBox("ERROR - invalid input...", RED)
		return
	
	try:
		gotoxy(1,6); printColored("Product ID: ", themeColor); 	productId = int(input())
		product:Product = inventory.getProductById(productId)
		gotoxy(5,6); printDarkGray(product)
	except:
		drawInfoBox("ERROR - invalid input...", RED)
		return

	gotoxy(1,7); printColored("Quantity:   ", themeColor); 	quantity = float(input())
	gotoxy(1,8); printColored("Discount:   ", themeColor); 	discount = float(input())

	try:
		sale = Sale(0, saleDate, clientId, productId, quantity, discount)
		inventory.addSale(sale)
		drawInfoBox("SUCCESS - Sale created...")
	except:
		drawInfoBox("ERROR - failed at creating sale...", RED)

	input()

def deleteSale(inventory:Inventory):
	clearScreen()
	printTitle("Canceling sale", themeColor)
	id = input("Sale ID: ")
	inventory.deleteSale(id)
	input()
