from Client import Client
from Sale import Sale
from Product import Product

from Inventory import Inventory

from TextUtils import *

themeColor = RED

def listClients(inventory:Inventory):
	clearScreen()
	printTitle(" Listing clients ", themeColor)
	clients = inventory.getClients()
	gotoxy(1,4)
	printColored(f"   {"ID":10} {"Name":30} {"E-mail":30} {"Phone":20}",themeColor)
	for i in range(len(clients)):
		c: Client = clients[i]
		print(f"   {str(c.id):10} {c.name:30} {c.email:30} {c.phone:20}")
	input()

def addClient(inventory:Inventory):
	clearScreen()
	printTitle("Adding new client", themeColor)
	
	gotoxy(2,4); printColored("Name: ",themeColor,end=""); name = input()
	if name == "": drawInfoBox("ERROR - Invalid Input, returning to menu...", RED); input(); return
	
	gotoxy(2,5); printColored("Email: ",themeColor,end=""); email = input()
	if email == "": drawInfoBox("ERROR - Invalid Input, returning to menu...", RED); input(); return
	
	gotoxy(2,6); printColored("Phone: ",themeColor,end=""); phone = input()
	if phone == "": drawInfoBox("ERROR - Invalid Input, returning to menu...", RED); input(); return
	
	client = Client(0, name, email, phone)
	inventory.addClient(client)
	input()

def updateClient(inventory:Inventory):
	clearScreen()
	printTitle("Updating client",themeColor)
	
	while True:
		try:
			gotoxy(2,4); printColored("Client ID: ",themeColor,end=""); id = input()
			id = int(id)
			c:Client = inventory.getClientById(id)
			gotoxy(2,5); printDarkGray(f"[{c.id}] {c.name} ({c.email} / {c.phone})")
			break
		except: drawInfoBox("ERROR - didn't input a valid ID... please try again")

	gotoxy(2,7); printColored("Name: ",themeColor,end=""); name = input()
	if name == "": drawInfoBox("ERROR - Invalid Input, returning to menu...", RED); input(); return
	gotoxy(2,8); printColored("Email: ",themeColor,end=""); email = input()
	if email == "": drawInfoBox("ERROR - Invalid Input, returning to menu...", RED); input(); return
	gotoxy(2,9); printColored("Phone: ",themeColor,end=""); phone = input()
	if phone == "": drawInfoBox("ERROR - Invalid Input, returning to menu...", RED); input(); return
	
	try: 
		client = Client(id, name, email, phone)
		inventory.updateClient(client)
		drawInfoBox("SUCCESS - client data updated... ", GREEN)
	except:
		drawInfoBox("ERROR - client update failed... ", RED)
	input()

def deleteClient(inventory:Inventory):
	clearScreen()
	printTitle("Deleting client", themeColor)
	while True:
		try:
			gotoxy(2,4); printColored("Client ID: ",themeColor,end=""); id = input()
			id = int(id)
			c:Client = inventory.getClientById(id)
			gotoxy(2,5); printDarkGray(f"[{c.id}] {c.name} ({c.email} / {c.phone})")
			break
		except: drawInfoBox("ERROR - didn't input a valid ID... please try again")
	
	inventory.deleteClient(id)
	input()

def printClientDetails(inventory:Inventory):
	clearScreen()
	printTitle("Printing client details",themeColor)
	
	while True:
		try:
			gotoxy(2,4); printColored("Client ID: ",themeColor,end=""); id = input()
			id = int(id)
			c:Client = inventory.getClientById(id)
			gotoxy(2,5); printColored("Name:   ",themeColor,end=""); print(c.name)
			gotoxy(2,6); printColored("E-mail: ",themeColor,end=""); print(c.email)
			gotoxy(2,7); printColored("Phone:  ",themeColor,end=""); print(c.phone)
			break
		except: drawInfoBox("ERROR - didn't input a valid ID... please try again")
	
	sales = inventory.getSalesByClient(id)
	
	gotoxy(1,9); printColored("Sales",themeColor)
	gotoxy(3,10); printColored(f"{"Id":3} {"Date":10} {"Product":40} {"Quantity":10} {"Discount":10} {"Total"}",themeColor)
	
	for i in range(len(sales)):
		gotoxy(3,11+i)
		s:Sale = sales[i]
		p:Product = inventory.getProductById(s.productId)
		product = f"{p.id} - {p.name}"
		total = p.sellPrice * s.quantity * ((100 - s.discount) / 100)
		print(f"{s.id:3} {s.date:10} {product:40} {str(s.quantity):10} {f"{s.discount:.2f}%":10} R$ {total:.2f}")
	input()
