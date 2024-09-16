from Product import Product
from Purchase import Purchase
from Sale import Sale

from Inventory import Inventory
from TextUtils import *

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
	drawInfoBox("Product Sucessfully Added!", GREEN)
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

	gotoxy(22,5); id = int(input())
	selectedProduct = inventory.getProductById(id)
	if selectedProduct is None:
		drawInfoBox("ERROR: Product doesn't exist!",RED)
		input()
		return

	gotoxy(22,8);  printDarkGray(selectedProduct.name)
	gotoxy(22,11); printDarkGray(f"{selectedProduct.buyPrice:.2f}")
	gotoxy(22,14); printDarkGray(f"{selectedProduct.sellPrice:.2f}")

	gotoxy(22,8);  name = input()
	gotoxy(22,11); buyPrice = float(input())
	gotoxy(22,14); sellPrice = float(input())
	
	product = Product(id, name, buyPrice, sellPrice)
	inventory.updateProduct(product)

	drawInfoBox("SUCCESS: Product updated! Press ENTER to proceed...", GREEN)
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